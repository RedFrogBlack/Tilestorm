#!/usr/bin/env python3
"""
TileStorm Multiplayer Server
WebSocket rooms for Duel / Hazard Wars / Co-op
"""
import asyncio, json, random, string, time
import websockets
from websockets.server import WebSocketServerProtocol

# ── Room state ──────────────────────────────────────────────────────
rooms = {}   # code -> { mode, players: [ws, ws], state: {} }

def gen_code():
    chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'
    while True:
        code = ''.join(random.choices(chars, k=4))
        if code not in rooms:
            return code

async def send(ws, msg):
    try:
        await ws.send(json.dumps(msg))
    except:
        pass

async def broadcast(room, msg, exclude=None):
    for p in room['players']:
        if p and p != exclude:
            await send(p, msg)

# ── Message handlers ────────────────────────────────────────────────
async def handle_create(ws, data):
    code = gen_code()
    mode = data.get('mode', 'duel')
    rooms[code] = {
        'mode': mode,
        'players': [ws, None],
        'ready': [False, False],
        'started': False,
        'state': {
            'scores': [0, 0],
            'lines':  [0, 0],
            'grids':  [None, None],
        },
        'created': time.time()
    }
    ws._room_code = code
    ws._player_idx = 0
    await send(ws, {'type': 'room_created', 'code': code, 'mode': mode, 'player': 0})

async def handle_join(ws, data):
    code = data.get('code', '').upper().strip()
    if code not in rooms:
        await send(ws, {'type': 'error', 'msg': 'Room not found. Check the code and try again.'})
        return
    room = rooms[code]
    if room['players'][1] is not None:
        await send(ws, {'type': 'error', 'msg': 'Room is full.'})
        return
    if room['started']:
        await send(ws, {'type': 'error', 'msg': 'Game already in progress.'})
        return
    room['players'][1] = ws
    ws._room_code = code
    ws._player_idx = 1
    # Tell both players
    await send(ws, {'type': 'joined', 'code': code, 'mode': room['mode'], 'player': 1})
    await send(room['players'][0], {'type': 'opponent_joined', 'mode': room['mode']})

async def handle_ready(ws, data):
    code = getattr(ws, '_room_code', None)
    if not code or code not in rooms: return
    room = rooms[code]
    idx = ws._player_idx
    room['ready'][idx] = True
    # If both ready, start
    if all(room['ready']) and not room['started']:
        room['started'] = True
        await broadcast(room, {'type': 'game_start', 'mode': room['mode']})

async def handle_update(ws, data):
    code = getattr(ws, '_room_code', None)
    if not code or code not in rooms: return
    room = rooms[code]
    idx = ws._player_idx
    # Store state
    if 'score' in data: room['state']['scores'][idx] = data['score']
    if 'lines' in data: room['state']['lines'][idx] = data['lines']
    if 'grid'  in data: room['state']['grids'][idx]  = data['grid']
    # Relay to opponent
    opp = room['players'][1 - idx]
    if opp:
        await send(opp, {
            'type': 'opponent_update',
            'score': room['state']['scores'][idx],
            'lines': room['state']['lines'][idx],
            'grid':  data.get('grid'),
        })

async def handle_attack(ws, data):
    """Hazard Wars: relay a tile-eat attack to the opponent"""
    code = getattr(ws, '_room_code', None)
    if not code or code not in rooms: return
    room = rooms[code]
    idx = ws._player_idx
    opp = room['players'][1 - idx]
    if opp:
        await send(opp, {'type': 'attack', 'count': data.get('count', 4)})

async def handle_coop_place(ws, data):
    """Co-op: player placed a piece — broadcast to partner"""
    code = getattr(ws, '_room_code', None)
    if not code or code not in rooms: return
    room = rooms[code]
    await broadcast(room, {
        'type': 'coop_place',
        'shape': data['shape'],
        'color': data['color'],
        'row':   data['row'],
        'col':   data['col'],
        'player': ws._player_idx,
    })

async def handle_emoji(ws, data):
    """Relay an emoji reaction to the opponent"""
    code = getattr(ws, '_room_code', None)
    if not code or code not in rooms: return
    room = rooms[code]
    idx = ws._player_idx
    opp = room['players'][1 - idx]
    emoji = data.get('emoji', '🐸')
    # Whitelist to prevent abuse
    allowed = ['😂','🔥','💀','👑','😤','🐸']
    if emoji not in allowed: emoji = '🐸'
    if opp:
        await send(opp, {'type': 'emoji_reaction', 'emoji': emoji, 'from': idx})

async def handle_game_over(ws, data):
    code = getattr(ws, '_room_code', None)
    if not code or code not in rooms: return
    room = rooms[code]
    idx = ws._player_idx
    await broadcast(room, {
        'type': 'player_game_over',
        'player': idx,
        'score': data.get('score', 0),
        'lines': data.get('lines', 0),
    })

# ── Connection lifecycle ─────────────────────────────────────────────
async def handler(ws: WebSocketServerProtocol):
    ws._room_code = None
    ws._player_idx = -1
    try:
        async for raw in ws:
            try:
                data = json.loads(raw)
            except:
                continue
            t = data.get('type')
            if   t == 'create':     await handle_create(ws, data)
            elif t == 'join':       await handle_join(ws, data)
            elif t == 'ready':      await handle_ready(ws, data)
            elif t == 'update':     await handle_update(ws, data)
            elif t == 'attack':     await handle_attack(ws, data)
            elif t == 'coop_place': await handle_coop_place(ws, data)
            elif t == 'emoji':      await handle_emoji(ws, data)
            elif t == 'game_over':  await handle_game_over(ws, data)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        # Notify partner of disconnect
        code = ws._room_code
        if code and code in rooms:
            room = rooms[code]
            idx  = ws._player_idx
            if idx >= 0 and idx < len(room['players']):
                room['players'][idx] = None
            await broadcast(room, {'type': 'opponent_disconnected'})
            # Clean up empty rooms
            if all(p is None for p in room['players']):
                del rooms[code]

async def cleanup_old_rooms():
    """Remove rooms older than 2 hours with no activity"""
    while True:
        await asyncio.sleep(600)
        now = time.time()
        stale = [c for c, r in rooms.items() if now - r['created'] > 7200]
        for c in stale:
            del rooms[c]

async def main():
    asyncio.create_task(cleanup_old_rooms())
    async with websockets.serve(handler, '0.0.0.0', 8765, ping_interval=20, ping_timeout=60):
        print('TileStorm WS server running on port 8765')
        await asyncio.Future()

asyncio.run(main())
