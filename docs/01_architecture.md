# TileStorm — Technical Architecture Document

**Project:** TileStorm  
**Brand:** RedFrogBlackArt (RFBA) — [redfrogblackart.com](https://redfrogblackart.com)  
**Live URL:** [https://www.perplexity.ai/computer/a/tilestorm-lNFITTzoTAmY.H9NxO57bQ](https://www.perplexity.ai/computer/a/tilestorm-lNFITTzoTAmY.H9NxO57bQ)  
**GitHub:** [https://github.com/q2rnnyz2wv-create/tilestorm](https://github.com/q2rnnyz2wv-create/tilestorm) *(private)*  
**Document version:** 1.0  

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [File Structure](#2-file-structure)
3. [Architecture Diagram](#3-architecture-diagram)
4. [Frontend Architecture](#4-frontend-architecture)
5. [Game Engine](#5-game-engine)
6. [Monetisation System](#6-monetisation-system)
7. [Multiplayer (Duo) Architecture](#7-multiplayer-duo-architecture)
8. [Deployment](#8-deployment)
9. [Security Considerations](#9-security-considerations)
10. [Known Issues & TODOs Before Launch](#10-known-issues--todos-before-launch)

---

## 1. System Overview

TileStorm is a tile-placement puzzle game delivered as a **single-page application (SPA)** with zero build-step, zero framework, and zero external runtime dependencies beyond two Google Fonts. The entire client — HTML markup, CSS styling, game logic, UI state machine, monetisation, and multiplayer WebSocket client — lives in a single `index.html` file (~4,100 lines).

### Key design decisions

| Decision | Rationale |
|---|---|
| Single-file HTML | Minimal deployment surface; no bundler or CI/CD required; trivially hostable on any static CDN |
| Vanilla ES6 JavaScript | No framework overhead; full control over rendering loop; no dependency churn |
| Canvas rendering | Hardware-accelerated 2D board; fine-grained control over cell drawing and animation |
| localStorage for state | Frictionless — no account creation required for trial or purchased tiers |
| WebSocket multiplayer | Low-latency real-time Duo modes; thin Python asyncio server handles room routing |

### Brand identity

- **Logo:** `rfba-logo.png` — white frog silhouette on transparent background
- **Brand name:** RedFrogBlackArt (RFBA)
- **Brand red:** `#CC1212`
- **Dark background:** `#080808`
- **Display font:** Orbitron (Google Fonts)
- **Body font:** Inter (Google Fonts)

---

## 2. File Structure

```
tilestorm/
├── index.html        # Entire game — HTML + CSS + JS (~4,100 lines)
├── rfba-logo.png     # White frog logo (transparent background)
├── server.py         # WebSocket server for Duo multiplayer
├── .gitignore
└── README.md         # (to be added)
```

### File responsibilities

#### `index.html`
The monolithic game client. Contains, in order:
1. `<head>` — meta tags, viewport, Google Fonts links, PWA manifest meta, inline `<style>` block (~600 lines of CSS)
2. `<body>` — all screen `<div>` elements (title, solo setup, game, game-over, duo lobby)
3. `<script>` — all game logic, engine, UI, monetisation, and WebSocket client code (~3,000+ lines)

#### `rfba-logo.png`
Static brand asset. Served alongside `index.html` from the same CDN bucket. Referenced in the title screen and potentially the PWA manifest.

#### `server.py`
Lightweight Python 3 WebSocket server using `asyncio` and the `websockets` library. Manages multiplayer rooms by 6-digit code. Does **not** serve static files — `index.html` is served separately via CDN.

#### `.gitignore`
Standard ignore rules for Python (`__pycache__`, `.pyc`, virtual environments) and OS artefacts.

---

## 3. Architecture Diagram

### Runtime architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                          User's Browser                              │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                        index.html                            │   │
│  │                                                              │   │
│  │  ┌─────────────────┐   ┌──────────────┐   ┌─────────────┐  │   │
│  │  │  Canvas Game    │   │  Screen /    │   │  Audio      │  │   │
│  │  │  Engine         │   │  UI State    │   │  Engine     │  │   │
│  │  │  (drawGrid,     │   │  Machine     │   │  (Web Audio │  │   │
│  │  │  pieces, combo) │   │  (showScreen)│   │   API)      │  │   │
│  │  └────────┬────────┘   └──────┬───────┘   └─────────────┘  │   │
│  │           │                   │                              │   │
│  │  ┌────────▼───────────────────▼──────────────────────────┐  │   │
│  │  │              Game Logic & State                        │  │   │
│  │  │  (scoring, combos, special bricks, challenge modes)    │  │   │
│  │  └────────────────────────┬──────────────────────────────┘  │   │
│  │                           │                                  │   │
│  │  ┌────────────────┐   ┌───▼──────────────────────────────┐  │   │
│  │  │  localStorage  │◄──│  Monetisation Layer              │  │   │
│  │  │                │   │  (initTrial, hasAccess,           │  │   │
│  │  │  ts_trial_start│   │   purchaseFromModal, TIERS[])     │  │   │
│  │  │  ts_owned_tiers│   └──────────────────────────────────┘  │   │
│  │  │  ts_equipped   │                                          │   │
│  │  └────────────────┘   ┌──────────────────────────────────┐  │   │
│  │                       │  WebSocket Client                 │  │   │
│  │                       │  (Duo multiplayer, WS_URL)        │  │   │
│  │                       └───────────────┬──────────────────┘  │   │
│  └───────────────────────────────────────┼──────────────────────┘   │
└──────────────────────────────────────────┼──────────────────────────┘
                                           │ WSS (WebSocket Secure)
                                           ▼
                          ┌────────────────────────────────┐
                          │        server.py               │
                          │  Python asyncio + websockets   │
                          │  Room management (6-digit code)│
                          │  Hosted: Fly.io or Railway     │
                          └────────────────────────────────┘
```

### Deployment pipeline

```
Developer (local edit)
        │
        │  git push
        ▼
┌───────────────────────┐
│  GitHub (private repo) │
│  github.com/q2rnnyz2wv│
│  -create/tilestorm    │
└──────────┬────────────┘
           │  Manual deploy (no CI/CD yet)
           │  deploy_website() via Perplexity Computer
           ▼
┌───────────────────────┐       ┌─────────────────────────────────┐
│  Perplexity Computer  │──────►│  S3 CDN (static asset bucket)   │
│  deploy_website tool  │       │  Asset ID: 94d1484d-3ce8-...    │
└───────────────────────┘       └──────────────┬──────────────────┘
                                               │  HTTPS
                                               ▼
                                ┌──────────────────────────────────┐
                                │  Browser                         │
                                │  perplexity.ai/computer/a/       │
                                │  tilestorm-lNFITTzoTAmY.H9NxO57bQ│
                                └──────────────────────────────────┘
```

---

## 4. Frontend Architecture

### Technology stack

| Layer | Technology |
|---|---|
| Language | Vanilla JavaScript (ES6+) — no transpiler, no TypeScript |
| Rendering | HTML5 Canvas 2D API |
| Styling | Inline `<style>` block with CSS custom properties |
| Fonts | Google Fonts CDN — Orbitron (display), Inter (body) |
| Storage | `window.localStorage` |
| Real-time comms | `WebSocket` (native browser API) |
| Audio | Web Audio API (`AudioContext`) |
| Animation | `requestAnimationFrame` loop |

### CSS design tokens

CSS custom properties are declared on `:root` and consumed throughout the stylesheet:

```css
:root {
  --red:          #CC1212;   /* RFBA brand red — CTAs, highlights */
  --bg:           #080808;   /* Primary dark background */
  --font-display: 'Orbitron', sans-serif;
  --font-body:    'Inter', sans-serif;
}
```

### Screen state machine

UI state is managed by the `showScreen(id)` function. All screen `<div>` elements coexist in the DOM; `showScreen` toggles the `.hidden` CSS class to show exactly one screen at a time.

```
showScreen(id)
  │
  ├── Adds .hidden to all screens
  └── Removes .hidden from document.getElementById(id)
```

**Registered screen IDs:**

| Screen ID | Purpose |
|---|---|
| `screen-title` | Main menu / landing screen |
| `screen-solo-setup` | Difficulty and mode selection before a solo game |
| `screen-game` | Active gameplay — canvas board + HUD |
| `screen-gameover` | End-of-game score summary |
| `screen-duo-lobby` | Multiplayer room creation / join flow |

### Canvas game board

The board is rendered onto an HTML `<canvas>` element. `calcLayout()` is called on load and on `window.resize` to recalculate cell dimensions from the current viewport size, ensuring the grid fills available screen space responsively.

```javascript
calcLayout()
  └── Computes cellSize = Math.floor(availableHeight / ROWS)
      └── Sets canvas.width  = cellSize * COLS
          Sets canvas.height = cellSize * ROWS
```

`drawGrid()` is the primary render function. It redraws the full board state every frame.

### Particle system

A lightweight particle system runs on its own `requestAnimationFrame` loop:

- `animateParticles()` — iterates the active particle array, updates positions, decrements lifetimes, and removes expired particles
- Particles are spawned on line clears and special brick activations
- Rendering is done on a separate overlay canvas or directly on the main canvas (z-ordered above the board)

### Audio engine

```javascript
ensureAudio()
  └── Called on first user interaction (click/touch)
      └── Creates AudioContext (resumes if suspended)
          └── All subsequent sound synthesis uses this context
```

Web Audio API is used for procedural audio synthesis — no external audio files are required, keeping the single-file architecture intact.

---

## 5. Game Engine

### Board dimensions

| Property | Value |
|---|---|
| Columns | 8 |
| Rows | 12 |
| Total cells | 96 |
| Layout | Recalculated by `calcLayout()` on every resize |

### Piece definitions

22 distinct shapes are defined as 2D boolean arrays (tetromino-style matrices of varying sizes). Each piece has:
- A shape matrix
- A colour assignment
- A tier association (some pieces are locked behind paid tiers)

### Input handling

Pieces are placed via **drag-and-drop** on the canvas, with full **touch support** for mobile:

| Event | Desktop | Mobile |
|---|---|---|
| Pick up piece | `mousedown` | `touchstart` |
| Drag | `mousemove` | `touchmove` |
| Place | `mouseup` | `touchend` |

Hit detection converts pointer coordinates to grid cell indices using the `cellSize` computed by `calcLayout()`.

### Scoring system

```
score += basePoints × difficultyMultiplier × tierBonusMultiplier
```

| Factor | Description |
|---|---|
| `basePoints` | Points per cell occupied by a placed piece |
| `difficultyMultiplier` | Scales with selected difficulty (Easy → Legendary) |
| `tierBonusMultiplier` | Higher tiers unlock bonus score multipliers |
| Combo bonus | Each consecutive clear increments the combo counter; score multiplies accordingly |

### Line clear mechanics

Both **full rows** and **full columns** trigger a clear event. When a row or column is completely filled:
1. The clear animation plays (particles, flash)
2. Cells are removed
3. Gravity is applied (remaining pieces shift)
4. Combo counter increments
5. Score is updated

### Combo system

```
comboCount++  on each consecutive clear
comboCount = 0  when a piece is placed without triggering a clear
```

The combo multiplier is applied on top of the base score for each clear within an active combo streak.

### Special bricks

| Brick | Behaviour |
|---|---|
| **Morph** | 2×2 wildcard — fills any gap, acts as any colour for line-clear checks |
| **Meteor** | Clears the fullest row on the board immediately |
| **Angel** | Fills the emptiest row, helping the player avoid board-lock |

Special bricks are awarded based on gameplay milestones or unlocked via paid tiers.

### Challenge modes

| Mode | Rule | Tier required |
|---|---|---|
| **Standard** | Classic — no time limit, clear to score | Froglet+ |
| **Frenzy** | 25-second timer per turn — place fast or lose | Treefrog+ |
| **Survival** | Board fill capped at 60% — exceed it and the game ends | Treefrog+ |
| **Colour Run** | Clear lines by matching 4 cells of the same colour | Poison Dart+ |

---

## 6. Monetisation System

> **Critical note:** Payment processing is **not yet integrated**. Purchases are currently simulated client-side. Real payment handling (Stripe or equivalent) **must** be integrated and server-side verified before charging real users.

### Trial model

On first launch, `initTrial()` records the current timestamp in `localStorage`:

```javascript
localStorage.setItem('ts_trial_start', Date.now());
```

`trialActive()` checks whether the current time is within 7 days of `ts_trial_start`.  
`trialDaysLeft()` returns the integer number of days remaining in the trial.

### Tier definitions (`TIERS` array)

| Tier key | Price | Unlocks |
|---|---|---|
| `tadpole` | Free (7-day trial) | Basic gameplay — Easy difficulty, Standard mode |
| `froglet` | £2.99 one-off | Easy + Standard (post-trial permanent access) |
| `treefrog` | £4.99 one-off | + Medium difficulty + Frenzy + Survival modes |
| `poisondart` | £7.99 one-off | + Hard difficulty + Colour Run + all power-ups |
| `goldenfrog` | £7.99 one-off | Legendary cosmetic tier (visual themes, effects) |
| `duopack` | £5/month | Multiplayer Duo modes |

### Access control functions

| Function | Purpose |
|---|---|
| `initTrial()` | Sets `ts_trial_start` in localStorage on first run |
| `trialActive()` | Returns `true` if within 7-day trial window |
| `trialDaysLeft()` | Returns integer days remaining in trial |
| `hasAccess(tierId)` | Returns `true` if `tierId` is in `ts_owned_tiers` or trial is active |
| `canPlayMedium()` | Checks Treefrog+ access |
| `canPlayHard()` | Checks Poison Dart+ access |
| `canPlayFrenzy()` | Checks Treefrog+ access |
| `canPlaySurvival()` | Checks Treefrog+ access |
| `canPlayColourRun()` | Checks Poison Dart+ access |
| `checkAccessBeforeStart()` | Gate called at game start — redirects to upgrade modal if access denied |
| `showUpgradeModal(reason)` | Renders the paywall modal with contextual reason string |
| `renderUpgradeTiers()` | Populates the upgrade modal with `TIERS` data |
| `purchaseFromModal(idx)` | Simulated purchase — writes tier to `ts_owned_tiers` in localStorage |
| `updateTrialBanner()` | Updates the trial countdown UI element |

### localStorage schema

| Key | Type | Description |
|---|---|---|
| `ts_trial_start` | `number` (Unix ms) | Timestamp of first launch — starts the 7-day trial |
| `ts_owned_tiers` | `JSON array` | Array of owned tier key strings, e.g. `["froglet","treefrog"]` |
| `ts_equipped` | `string` | Key of the currently equipped cosmetic tier |

### Purchase flow (current — simulated)

```
User clicks upgrade CTA
        │
        ▼
showUpgradeModal(reason)
        │
        ▼
renderUpgradeTiers() — renders TIERS[] as selectable cards
        │
        ▼
User clicks "Buy"
        │
        ▼
purchaseFromModal(idx)
  └── Pushes tier key into ts_owned_tiers in localStorage
      └── Closes modal, re-checks access
```

### Purchase flow (target — with Stripe)

```
User clicks "Buy"
        │
        ▼
Client calls Stripe Checkout / Payment Intent
        │
        ▼
Stripe webhook → backend endpoint
        │
        ▼
Backend verifies payment, issues signed token or writes to DB
        │
        ▼
Client receives confirmation → unlocks tier
```

---

## 7. Multiplayer (Duo) Architecture

### Overview

Duo multiplayer connects two players via a shared WebSocket server. The client in `index.html` initiates a WebSocket connection; `server.py` acts as a room broker and game-state relay.

### Server (`server.py`)

```python
# server.py — conceptual structure
import asyncio, websockets, json, random, string

rooms = {}   # { "ABC123": { "players": [ws1, ws2], "state": {...} } }

async def handler(websocket, path):
    # Dispatch on message type:
    # CREATE_ROOM  → generate 6-digit code, register room
    # JOIN_ROOM    → attach second player, start game
    # GAME_EVENT   → relay to opponent
    # LEAVE        → clean up room

asyncio.run(websockets.serve(handler, "0.0.0.0", PORT))
```

- **Language:** Python 3.10+
- **Libraries:** `asyncio`, `websockets`
- **Room code format:** 6 alphanumeric characters (e.g. `A3F9K2`)
- **Max players per room:** 2
- **Persistent state:** None — rooms are in-memory and destroyed on disconnect

### Duo game modes

| Mode | Description | Win condition |
|---|---|---|
| **Live Duel** | Competitive — players race on separate boards | First to clear 10 rows |
| **Hazard Wars** | Competitive — clearing lines sends attack tiles to opponent | Last board standing |
| **Co-op** | Cooperative — players share a single board | Achieve target score together |

### Room connection flow

```
Host browser                    server.py                   Guest browser
     │                              │                              │
     │── CREATE_ROOM ──────────────►│                              │
     │◄── { code: "A3F9K2" } ──────│                              │
     │                              │                              │
     │  (host shares code out-of-band, e.g. voice/chat)           │
     │                              │                              │
     │                              │◄─── JOIN_ROOM { code } ─────│
     │◄── PLAYER_JOINED ───────────►│──── PLAYER_JOINED ─────────►│
     │                              │                              │
     │◄═══════════ GAME_START ══════╪══════════════════════════════│
     │                              │                              │
     │── GAME_EVENT ───────────────►│──── GAME_EVENT ────────────►│
     │◄── GAME_EVENT ──────────────│◄─── GAME_EVENT ──────────────│
```

### WebSocket URL

> **Known issue:** `WS_URL` in `index.html` is currently hardcoded to an old Cloudflare tunnel that is **no longer active**. Multiplayer will not connect until the server is re-hosted and `WS_URL` is updated to the new endpoint.

The `WS_URL` constant should be updated to the production WebSocket server address once it is deployed to Fly.io or Railway.

### `isDuoSubscriber()` — launch blocker

```javascript
// CURRENT (WRONG — bypasses paywall):
function isDuoSubscriber() { return true; }

// TARGET (correct):
function isDuoSubscriber() {
  return hasAccess('duopack');
}
```

> **This must be corrected before launch.** All users currently bypass the £5/month Duo paywall.

### Recommended server hosting

| Platform | Notes |
|---|---|
| **Fly.io** | Free tier for small apps; persistent WebSocket support; global edge deployment |
| **Railway** | Simple `server.py` deploy via `Procfile`; auto-sleep on free tier (may cause reconnect latency) |

See the platforms document for full deployment instructions.

---

## 8. Deployment

### Static client (index.html + rfba-logo.png)

The game client is deployed as a static website via the **Perplexity Computer** `deploy_website` tool, which uploads files to an S3-backed CDN.

**Deploy command:**
```python
deploy_website(
    project_path = "/home/user/workspace/tilestorm",
    site_name    = "TileStorm",
    entry_point  = "index.html",
    should_validate = False
)
```

**Deployment details:**

| Property | Value |
|---|---|
| Asset ID | `94d1484d-3ce8-4c09-98f8-7f4dc4ee7b6d` |
| Live URL | https://www.perplexity.ai/computer/a/tilestorm-lNFITTzoTAmY.H9NxO57bQ |
| CDN | S3-backed Perplexity Computer static hosting |
| HTTPS | Provided by CDN layer (no configuration required) |

### Source control

| Property | Value |
|---|---|
| Repository | https://github.com/q2rnnyz2wv-create/tilestorm |
| Visibility | Private |
| CI/CD | None — manual deploy only |

### Deployment workflow (current — manual)

```
1. Edit index.html or server.py locally
2. git add . && git commit -m "..." && git push
3. In Perplexity Computer session:
   → Call deploy_website() with parameters above
4. Verify live URL reflects changes
```

### Deployment workflow (recommended — automated)

A future CI/CD pipeline could be added using GitHub Actions:

```yaml
# .github/workflows/deploy.yml (proposed)
on:
  push:
    branches: [main]
jobs:
  deploy:
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to CDN
        # Call deploy_website via Perplexity Computer API or equivalent
```

---

## 9. Security Considerations

### Current state and risks

| Area | Risk | Severity |
|---|---|---|
| **Purchase state in localStorage** | `ts_owned_tiers` can be written manually in DevTools to unlock all tiers for free | High |
| **No backend auth** | All game state and entitlements are client-side — no server-side validation | High |
| **`isDuoSubscriber()` hardcoded** | All users have free Duo access — revenue impact | High |
| **WebSocket input validation** | `server.py` does not yet validate message schemas or enforce rate limits — DoS risk | Medium |
| **No GDPR consent flow** | Required before collecting any data from UK/EU users | Medium |
| **VAT** | Not yet registered — required at the UK VAT threshold | Low (pre-launch) |
| **No HTTPS enforcement on WS server** | WebSocket server must use `wss://` (TLS) in production | Medium |

### Required mitigations before launch

#### 1. Server-side payment verification
Move tier entitlements off localStorage. After a successful Stripe payment:
- Stripe webhook fires to a backend endpoint
- Backend stores the purchase against a user identifier (email or UUID)
- Client fetches entitlements from the backend on load
- Entitlements are signed (JWT or session cookie) to prevent client-side spoofing

#### 2. WebSocket hardening
```python
# server.py — add before production:
# - Schema validation on all incoming JSON messages
# - Per-connection rate limiting (max N messages/second)
# - Maximum room lifetime / idle timeout
# - Input length caps on all string fields (room codes, usernames)
```

#### 3. GDPR consent banner
Before any localStorage writes (including `ts_trial_start`), display a consent banner that:
- Explains what data is stored and why
- Links to a Privacy Policy
- Obtains explicit consent before setting any non-essential storage

#### 4. Content Security Policy
Add a `Content-Security-Policy` header (or `<meta>` tag) to restrict resource loading to known origins:
```html
<meta http-equiv="Content-Security-Policy"
      content="default-src 'self'; connect-src wss://your-server.fly.dev;
               font-src https://fonts.gstatic.com; style-src 'self' 'unsafe-inline'
               https://fonts.googleapis.com;">
```

---

## 10. Known Issues & TODOs Before Launch

### Critical (must fix before charging real users)

- [ ] **WebSocket server has no permanent host** — `WS_URL` points to a defunct Cloudflare tunnel. Deploy `server.py` to Fly.io or Railway and update `WS_URL` in `index.html`.
- [ ] **`isDuoSubscriber()` hardcoded to `true`** — revert to `return hasAccess('duopack')` before launch. All users currently bypass the £5/month subscription gate.
- [ ] **Payment processing not integrated** — `purchaseFromModal()` simulates purchases client-side. Integrate Stripe (or RevenueCat for mobile) with server-side webhook verification before accepting real payments.
- [ ] **No real authentication** — tier purchases are stored only in `localStorage` and are trivially spoofable. Implement server-side entitlement storage tied to a user identity.

### Important (fix before public marketing)

- [ ] **GDPR consent banner** — required before storing `ts_trial_start` or any other data for UK/EU users. Implement opt-in consent flow with a Privacy Policy page.
- [ ] **VAT registration** — required once revenue exceeds the UK VAT threshold (currently £90,000). Owner is aware and will register at the appropriate time.

### Nice-to-have (post-launch polish)

- [ ] **Mobile touch target sizes** — some UI buttons may be below Apple's recommended 44×44pt minimum tap target. Audit and increase padding on affected controls.
- [ ] **CI/CD pipeline** — set up GitHub Actions to automate deployment to the CDN on push to `main`, eliminating the manual Perplexity Computer deploy step.
- [ ] **README.md** — add a project README to the repository covering local development, deployment, and multiplayer server setup.
- [ ] **WebSocket reconnection logic** — client should attempt automatic reconnect with exponential backoff if the WebSocket connection drops mid-game.
- [ ] **Error boundaries** — wrap game loop in try/catch to prevent silent failures from breaking the canvas render loop.

---

*Document maintained by RedFrogBlackArt (RFBA). Last updated: 2025.*
