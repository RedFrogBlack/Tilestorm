# TileStorm — Data Flows

All data flows in TileStorm: how data moves through the application, where it is stored, and how multiplayer synchronisation works.

---

## localStorage Keys

| Key | Type | Set When | Used For |
|-----|------|----------|----------|
| `ts_trial_start` | Number (timestamp) | First ever game launch | Trial countdown. If absent, `initTrial()` sets it to `Date.now()` |
| `ts_owned_tiers` | JSON array string | After `confirmPurchase()` | List of owned tier IDs, e.g. `["froglet","treefrog"]` |
| `ts_equipped` | String | After `confirmPurchase()` or `equipTier()` | Currently equipped tier ID |
| `ts_best` | Number | After each game ends | All-time best score |
| `ts_streak_last` | String (date) | Daily on game launch | Last play date, used for streak calculation |
| `ts_streak_count` | Number | Daily on game launch | Current daily streak count |

---

## Trial Flow

```
User opens game (first time)
  └─ initTrial()
       └─ checks localStorage for ts_trial_start
            └─ not found → sets ts_trial_start = Date.now()

Every time home screen loads
  └─ updateTrialBanner()
       └─ trialDaysLeft() = Math.ceil((ts_trial_start + 7days - now) / 1day)
       └─ trialActive() = trialDaysLeft() > 0

hasAccess(tierId)
  └─ if trialActive() → return true  (full access during trial)
  └─ else → check ts_owned_tiers for tierId

After 7 days
  └─ trialActive() = false
  └─ canPlayMedium / canPlayHard / canPlayFrenzy / canPlaySurvival / canPlayColourRun → all return false
       unless the relevant tier is present in ts_owned_tiers

checkAccessBeforeStart()
  └─ if trial expired AND no paid tier owned → showUpgradeModal() → return false
  └─ game does not start
```

### Step-by-step

1. User opens the game for the first time → `initTrial()` checks for `ts_trial_start` → not found → sets `ts_trial_start = Date.now()`.
2. Every time the home screen is shown → `updateTrialBanner()` → `trialDaysLeft() = Math.ceil((ts_trial_start + 7days - now) / 1day)`.
3. `trialActive()` returns `true` while `trialDaysLeft() > 0`.
4. `hasAccess(tierId)` → if `trialActive()` returns `true`, grant full access regardless of owned tiers.
5. After 7 days → `trialActive()` returns `false` → all `canPlay*` gate functions return `false` unless the relevant tier is owned.
6. `checkAccessBeforeStart()` → if the trial has expired and no paid tier is owned → calls `showUpgradeModal()` → returns `false` → game does not start.

---

## Purchase Flow (Current — Simulated)

```
User taps locked feature
  └─ showUpgradeModal(reason)
       └─ User taps price button
            └─ purchaseFromModal(idx) → opens shop

User taps BUY in shop
  └─ openPurchaseModal(tierIdx)
       └─ User confirms
            └─ confirmPurchase()
                 ├─ Adds tier to ownedTiers array
                 ├─ saveOwnedTiers()
                 │    ├─ localStorage.setItem('ts_owned_tiers', JSON.stringify(ownedTiers))
                 │    └─ localStorage.setItem('ts_equipped', equippedTierId)
                 ├─ updateTrialBanner()
                 └─ updateLockIcons()
```

### Step-by-step

1. User taps a locked feature → `showUpgradeModal(reason)` is called.
2. User taps a price button in the modal → `purchaseFromModal(idx)` → shop opens.
3. User taps BUY in the shop → `openPurchaseModal(tierIdx)`.
4. User confirms → `confirmPurchase()`:
   - Adds the tier to the in-memory `ownedTiers` array.
   - Calls `saveOwnedTiers()` which writes `ts_owned_tiers` and `ts_equipped` to localStorage.
   - Calls `updateTrialBanner()` to refresh the home screen pill.
   - Calls `updateLockIcons()` to unlock the relevant buttons.

---

## Purchase Flow (Future — Real Payment)

```
User taps BUY
  └─ Call Stripe Checkout or RevenueCat purchase API
       └─ On payment success callback
            ├─ Call confirmPurchase() (or equivalent) to update local state
            ├─ Store purchase receipt server-side against user ID
            └─ On next load → fetch owned tiers from server, not just localStorage
```

### What needs to change

1. Replace the `confirmPurchase()` body with a call to **Stripe Checkout** or **RevenueCat**.
2. On the payment success callback, call `confirmPurchase()` (or an equivalent function) to update local UI state.
3. Store the purchase receipt server-side, tied to a user ID.
4. On each app load, fetch the user's owned tiers from the server and reconcile with localStorage (so purchases survive a browser clear).

---

## WebSocket Data Flow (Duo Multiplayer)

The WebSocket server (`server.py`) runs on port 8765 and manages rooms entirely in memory.

```
Host clicks CREATE ROOM
  └─ Client sends: { type: "create_room" }
       └─ Server generates a 6-digit code
            └─ Server sends: { type: "room_created", code: "ABC123" } → to host

Guest enters code
  └─ Client sends: { type: "join_room", code: "ABC123" }
       └─ Server pairs both clients
            └─ Server sends: { type: "room_ready" } → to both players

During game (every piece placement)
  └─ Each client sends: board state + current score
       └─ Server broadcasts the payload to the other player in the room

Hazard events
  └─ Sending client sends: { type: "hazard", rows: 2 }
       └─ Server forwards to opponent

Game end
  └─ Ending client sends: { type: "game_over", score: X }
       └─ Server forwards to the other player
            └─ Server declares winner based on scores
```

### Message reference

| Direction | Message type | Payload fields | Purpose |
|-----------|-------------|----------------|---------|
| Client → Server | `create_room` | — | Host requests a new room |
| Server → Client | `room_created` | `code` | Returns the 6-digit room code to host |
| Client → Server | `join_room` | `code` | Guest joins an existing room |
| Server → Client | `room_ready` | — | Sent to both players when room is full |
| Client → Server | *(board update)* | board state, score | Sent on each piece placement |
| Server → Client | *(board update)* | board state, score | Forwarded to opponent |
| Client → Server | `hazard` | `rows` | Sends a hazard to opponent |
| Server → Client | `hazard` | `rows` | Forwarded to opponent |
| Client → Server | `game_over` | `score` | Reports final score |
| Server → Client | `game_over` | `score` | Forwarded; server declares winner |

---

## Score & Streak Flow

### Score

```
placePiece()
  └─ checkLines() — counts completed lines
       └─ updateScore()
            └─ points = base points × difficulty multiplier × tier bonus
                 └─ if points > ts_best → localStorage.setItem('ts_best', points)
```

- Base points are calculated per line cleared.
- A **difficulty multiplier** is applied based on the selected difficulty setting (`DIFF_SETTINGS`).
- A **tier bonus** is applied based on the currently equipped tier.
- On game over, the final score is compared to `ts_best` in localStorage and updated if it is a new record.

### Streak

```
Game launches (loadStreak())
  └─ Read ts_streak_last and ts_streak_count from localStorage
       ├─ ts_streak_last === yesterday → increment ts_streak_count, update ts_streak_last to today
       ├─ ts_streak_last === today     → no change (already counted today)
       └─ ts_streak_last is 2+ days ago (or absent) → reset ts_streak_count to 1, set ts_streak_last to today
```

- `ts_streak_last` stores the date string of the last session.
- `ts_streak_count` stores the running consecutive-day count.
- The streak resets to 1 if the player misses any calendar day.
