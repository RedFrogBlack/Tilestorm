# TileStorm — Features & Capabilities Reference

> **Audience:** Developers and game owners who need a complete, authoritative reference for every feature, tier, UI element, and game mechanic in TileStorm.

---

## Table of Contents

1. [Trial & Access Model](#1-trial--access-model)
2. [Tier Overview](#2-tier-overview)
3. [Tier Details](#3-tier-details)
4. [Difficulty Settings](#4-difficulty-settings)
5. [Challenge Modes](#5-challenge-modes)
6. [Power-Ups](#6-power-ups)
7. [Special Bricks (Bonus Bricks)](#7-special-bricks-bonus-bricks)
8. [Multiplayer — Duo Pack](#8-multiplayer--duo-pack)
9. [Screen-by-Screen UI Reference](#9-screen-by-screen-ui-reference)
   - [Home Screen](#91-home-screen)
   - [Solo Setup Screen](#92-solo-setup-screen)
   - [In-Game Screen](#93-in-game-screen)
   - [Game Over Screen](#94-game-over-screen)
   - [Duo Lobby](#95-duo-lobby)
   - [Shop](#96-shop)
   - [Upgrade Modal](#97-upgrade-modal)

---

## 1. Trial & Access Model

| Property | Detail |
|---|---|
| Trial tier name | **TADPOLE 🥚** |
| Duration | 7 days of full access to every feature |
| localStorage key | `ts_trial_start` (set on very first launch; never reset) |
| After trial expires | Player must purchase a paid tier to continue playing |
| Trial banner | Visible on the Home screen; shows days remaining, or an "upgrade" prompt once expired |

The trial gives new players a full taste of the game with no feature restrictions. Once the 7-day window closes, all gameplay is gated behind a tier purchase. The trial start date is stored in `localStorage` under `ts_trial_start` so it persists across sessions on the same device.

---

## 2. Tier Overview

| Tier | Name | Price | Cumulative Access |
|---|---|---|---|
| Trial | TADPOLE 🥚 | Free, 7 days | Everything (time-limited) |
| Tier 1 | FROGLET 🐟 | £2.99 one-off | Easy difficulty, Standard challenge, basic cosmetics |
| Tier 2 | TREE FROG 🐸 | £4.99 one-off | + Medium difficulty, Frenzy & Survival challenges, BOMB power-up |
| Tier 3 | POISON DART 🦎 | £7.99 one-off | + Hard difficulty, Colour Run, all power-ups, 1.5× bonus |
| Tier 4 | GOLDEN FROG ✨ | £7.99 one-off | Legendary cosmetic tier, 2.0× multiplier, STORM power-up |
| Duo Pack | DUO 🎮 | £5/month per player | Live multiplayer modes (both players must subscribe) |

> Tiers are **one-off purchases** (no subscription) except the Duo Pack, which is monthly per player. Tiers are cumulative — each tier includes everything from all tiers below it.

---

## 3. Tier Details

### Tier 1 — FROGLET 🐟 — £2.99 one-off

The entry-level paid tier. Suitable for casual players.

| Category | Detail |
|---|---|
| Difficulty | Easy only |
| Challenge mode | Standard only |
| Tile skin | Aqua shimmer |
| Grid theme | Ocean grid |
| Power-up | SPLASH — clears the fullest row (3 uses per game) |
| Score multiplier | 1.0× |

---

### Tier 2 — TREE FROG 🐸 — £4.99 one-off

Everything in Froglet, plus the following additions:

| Category | Detail |
|---|---|
| Difficulty | Medium (speed pieces + hazards, 1.3× score) |
| Challenge modes | Frenzy (clear 3 lines in 25s — repeating), Survival (keep board under 60% filled for 60s) |
| Tile skin | Neon green |
| Grid theme | Jungle canopy |
| Power-up | BOMB — blasts a 3×3 area (3 uses per game) |
| Mascot | Frog mascot displayed on the grid |

---

### Tier 3 — POISON DART 🦎 — £7.99 one-off

Everything in Tree Frog, plus:

| Category | Detail |
|---|---|
| Difficulty | Hard (vanishing tiles, 1.8× score) |
| Challenge mode | Colour Run (match 4 same-colour pieces consecutively) |
| Power-ups | All power-ups unlocked |
| Tile skin | Toxic gradient |
| Grid theme | Volcanic grid |
| Power-up | VENOM — wipes one entire colour from the board (5 uses per game) |
| Score bonus | Additional 1.5× score multiplier |

---

### Tier 4 — GOLDEN FROG ✨ — £7.99 one-off

A **legendary / cosmetic** tier. Primarily prestige and visual upgrades on top of Poison Dart.

| Category | Detail |
|---|---|
| Type | Cosmetic / prestige (no new gameplay modes) |
| Tile skin | Gold holographic tiles |
| Grid theme | Galaxy grid with animated starfield |
| Power-up | STORM — force-clears 2 lines (5 uses per game) |
| Score multiplier | 2.0× |
| Visual effects | Rainbow particles |
| Mascot | Golden frog mascot |

---

## 4. Difficulty Settings

Difficulty affects piece speed, hazard frequency, vanishing tiles, and the score multiplier.

| Difficulty | Hazard Chance | Hazard Frequency | Vanishing Tiles | Score Multiplier | Minimum Tier |
|---|---|---|---|---|---|
| Easy | None | None | No | 1.0× | Froglet+ |
| Medium | 18% | Every 25 pieces | No | 1.3× | Tree Frog+ |
| Hard | 32% | Every 15 pieces | Yes | 1.8× | Poison Dart+ |

- **Hazard bricks** are special board-disrupting tiles that appear among regular pieces.
- **Vanishing tiles** (Hard only) disappear from the board after a delay, forcing faster decisions.
- The score multiplier is applied on top of any tier-specific multiplier bonus.

---

## 5. Challenge Modes

Challenge modes replace the classic "endless" format with a specific win/fail condition. Players select a challenge mode on the Solo Setup screen.

| Mode | Description | Win / Fail Condition | Minimum Tier |
|---|---|---|---|
| Standard ⭐ | Classic Tetris-style play, no time limit | No fail condition beyond board filling | Any paid tier |
| Frenzy ⚡ | Clear 3 lines within 25 seconds | Timer resets each round; game ends if timer hits zero | Tree Frog+ |
| Survival 🛡️ | Keep the board below 60% filled for 60 seconds | Fails immediately if board reaches 60% fill | Tree Frog+ |
| Colour Run 🎨 | Match 4 same-colour pieces consecutively | Fail if streak is broken | Poison Dart+ |

- **Frenzy** repeats continuously — each cleared triple resets the 25s timer.
- **Survival** displays a fill-level bar in-game (the Survival bar HUD element).

---

## 6. Power-Ups

Power-ups are earned during play and activated via the power-up button in-game. Uses are capped per game. Higher tiers unlock more powerful power-ups.

| Power-Up | Icon | Effect | Uses per Game | Minimum Tier |
|---|---|---|---|---|
| SPLASH | 💧 | Clears the fullest row on the board | 3 | Froglet+ |
| BOMB | 💣 | Blasts a 3×3 area of tiles | 3 | Tree Frog+ |
| VENOM | ☠️ | Wipes every tile of one entire colour from the board | 5 | Poison Dart+ |
| STORM | ⚡ | Force-clears 2 lines instantly | 5 | Golden Frog+ |

- Players with **Poison Dart** unlock access to **all** power-ups simultaneously.
- Power-ups enter a queue and are activated by tapping the power-up button during a game.

---

## 7. Special Bricks (Bonus Bricks)

Special bricks appear among normal pieces and provide positive gameplay effects. They are distinct from hazard bricks.

| Brick | Icon | Effect | Minimum Tier |
|---|---|---|---|
| Morph | 🔮 | Wildcard — fills any 2×2 area the player chooses | Froglet+ |
| Meteor | ☄️ | Automatically clears the fullest row on the board | Earned by combo (3/5/8 hits) or every N pieces — no tier gate noted |
| Angel | 😇 | Fills the emptiest row with cleared (blank) tiles, easing pressure | Tree Frog+ |

- **Meteor** is the most accessible special brick, triggered by in-game combo milestones rather than tier ownership.
- **Morph** and **Angel** are gated by tier and will not appear for players below the required level.

---

## 8. Multiplayer — Duo Pack

The Duo Pack is a **monthly subscription** (£5/month per player). Both players in a session must independently hold an active Duo Pack subscription. Access is not transferable.

### Duo Modes

| Mode | Description |
|---|---|
| Live Duel | First player to clear 10 rows wins |
| Hazard Wars | Cleared lines send hazard bricks to the opponent's board |
| Co-op | Both players share a single board and survive together |

### Duo Features

| Feature | Detail |
|---|---|
| Room codes | 6-digit codes; any player can CREATE or JOIN a room |
| Connectivity | Works worldwide (room-code based, no friends list required) |
| Emoji reactions | In-game emoji tray (🔥💀👑😤😂🐸) to send reactions to opponent |
| Pricing | £5/month **per player** — both must pay independently |

---

## 9. Screen-by-Screen UI Reference

### 9.1 Home Screen

The main entry point of the game.

| Element | Type | Behaviour |
|---|---|---|
| **SOLO PLAY** | Button (red) | Navigates to the Solo Setup screen |
| **DUO PLAY** | Button (purple) | Navigates to the Duo Lobby screen |
| **Streak row** | Display | Shows 🔥 daily streak count |
| **Tier badge** | Display | Shows the currently equipped tier name and its colour dot |
| **Trial banner** | Display / tap target | Shows days remaining in trial; shows "upgrade" prompt after trial ends; tap opens the Upgrade Modal |
| **Title swatches** | Decorative | Colour dots in the RFBA rainbow palette — purely visual |
| **Best Score** | Display | Shows the player's all-time best score (bottom of screen) |

---

### 9.2 Solo Setup Screen

Reached from Home → SOLO PLAY. Players choose difficulty and challenge mode before starting.

| Element | Type | Behaviour |
|---|---|---|
| **← Back** | Button | Returns to the Home screen |
| **Easy 🟢** | Difficulty selector | Selects Easy — always available to any tier |
| **Medium 🟡** | Difficulty selector | Selects Medium — shows 🔒 if player does not own Tree Frog+; locked tapping has no effect (or shows modal) |
| **Hard 🟣** | Difficulty selector | Selects Hard — shows 🔒 if player does not own Poison Dart+ |
| **Standard ⭐** | Challenge selector | Selects Standard challenge — always available |
| **Frenzy ⚡** | Challenge selector | Selects Frenzy — locked if below Tree Frog; tapping opens the Upgrade Modal |
| **Survival 🛡️** | Challenge selector | Selects Survival — locked if below Tree Frog; tapping opens the Upgrade Modal |
| **Colour Run 🎨** | Challenge selector | Selects Colour Run — locked if below Poison Dart; tapping opens the Upgrade Modal |
| **▶ START GAME** | Button | Starts the game with selected settings; blocked with Upgrade Modal if trial has expired and no tier is owned |
| **FROG EVOLUTION SHOP ▾** | Shortcut button | Opens the Shop overlay directly |

**Lock behaviour:** Locked difficulty and challenge options display a 🔒 icon. Tapping a locked option opens the Upgrade Modal pointing to the required tier, rather than navigating away.

---

### 9.3 In-Game Screen

The active gameplay view.

| Element | Type | Behaviour |
|---|---|---|
| **Power-up button** (💧/💣/☠️/⚡) | Button | Activates the next earned power-up from the player's queue |
| **Pause / Menu button** | Button | Stops the game and returns to the Home screen |
| **Score display** | Display | Shows the live running score (top of screen) |
| **Level display** | Display | Shows the current game level |
| **Diff indicator** | Display | Shows EASY / MEDIUM / HARD badge |
| **Challenge HUD** | Display | Shows challenge mode name + countdown timer (visible in Frenzy and Survival modes only) |
| **Survival bar** | Display | Fill-level indicator showing how close the board is to 60% (Survival mode only) |
| **Emoji bar toggle 😊** | Button | Opens the emoji reaction tray (Duo mode only) |
| **Emoji buttons** (🔥💀👑😤😂🐸) | Buttons | Sends the selected emoji reaction to the opponent (Duo mode only) |

---

### 9.4 Game Over Screen

Shown when the game ends (board topped out or challenge failed).

| Element | Type | Behaviour |
|---|---|---|
| **Play Again** | Button | Immediately restarts a new game with the same difficulty and challenge settings |
| **Menu** | Button | Returns to the Home screen |

---

### 9.5 Duo Lobby

Reached from Home → DUO PLAY. Players create or join a multiplayer room.

| Element | Type | Behaviour |
|---|---|---|
| **← BACK** | Button | Returns to the Home screen |
| **CREATE ROOM** | Button | Generates a 6-digit room code; puts the player in a waiting state until a partner joins |
| **JOIN ROOM** | Button / input | Accepts a 6-digit code to join a partner's waiting room |
| **Live Duel** | Mode card | Selects Live Duel mode (first to 10 rows) |
| **Hazard Wars** | Mode card | Selects Hazard Wars mode (send hazard bricks to opponent) |
| **Co-op** | Mode card | Selects Co-op mode (shared board survival) |
| **Start Duo Game** | Button | Begins the multiplayer session once both players are connected and a mode is selected |

---

### 9.6 Shop

The purchase and cosmetic management screen. Accessible via the FROG EVOLUTION SHOP shortcut or the Upgrade Modal.

| Element | Type | Behaviour |
|---|---|---|
| **Tier cards** | Display | One card per paid tier (Froglet, Tree Frog, Poison Dart, Golden Frog) showing all perks |
| **BUY / UNLOCK button** | Button | Initiates purchase flow for that tier (currently simulated — no live payment processor) |
| **Equip button** | Button | Sets an already-owned tier as the active/displayed tier |
| **✕ Close** | Button | Closes the Shop overlay and returns to the previous screen |

---

### 9.7 Upgrade Modal

A contextual overlay that appears whenever a player attempts to use a feature they have not unlocked.

| Element | Type | Behaviour |
|---|---|---|
| **Reason header** | Display | Explains why the modal appeared (e.g. "Medium difficulty requires Tree Frog tier") |
| **Tier cards (×4)** | Display | Shows all four paid tiers with their price buttons |
| **OWNED badge** | Display | Green "OWNED ✓" badge on any tier the player already owns |
| **Price button** | Button | Opens the Shop scrolled/anchored to the tapped tier |
| **✕ / Tap outside** | Dismiss | Closes the modal without navigating away |

---

## Appendix — Tier Access Quick Reference

Use this table to quickly determine which tier is required for any feature.

| Feature | Free Trial | Froglet | Tree Frog | Poison Dart | Golden Frog |
|---|:---:|:---:|:---:|:---:|:---:|
| Easy difficulty | ✓ | ✓ | ✓ | ✓ | ✓ |
| Medium difficulty | ✓ | — | ✓ | ✓ | ✓ |
| Hard difficulty | ✓ | — | — | ✓ | ✓ |
| Standard challenge | ✓ | ✓ | ✓ | ✓ | ✓ |
| Frenzy challenge | ✓ | — | ✓ | ✓ | ✓ |
| Survival challenge | ✓ | — | ✓ | ✓ | ✓ |
| Colour Run challenge | ✓ | — | — | ✓ | ✓ |
| SPLASH power-up | ✓ | ✓ | ✓ | ✓ | ✓ |
| BOMB power-up | ✓ | — | ✓ | ✓ | ✓ |
| VENOM power-up | ✓ | — | — | ✓ | ✓ |
| STORM power-up | ✓ | — | — | — | ✓ |
| Morph special brick | ✓ | ✓ | ✓ | ✓ | ✓ |
| Angel special brick | ✓ | — | ✓ | ✓ | ✓ |
| Duo modes | ✓ | — | — | — | — (separate Duo Pack) |
| 2.0× multiplier | ✓ | — | — | — | ✓ |
| Gold holographic tiles | ✓ | — | — | — | ✓ |
| Galaxy grid | ✓ | — | — | — | ✓ |

> During the free trial, all features behave as if fully unlocked. After trial expiry, access reverts to only what the player has purchased.
