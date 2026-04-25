# TileStorm — Developer Handover Guide

> **Goal:** A developer with solid web skills but zero TileStorm context should be able to read this document and be productive within an hour.

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/q2rnnyz2wv-create/tilestorm
```

### Run the game (solo)

No build step. No `npm install`. No bundler.

Open `index.html` directly in a browser, or use the **VS Code Live Server** extension for auto-reload on save.

### Run the game (duo / multiplayer testing)

The WebSocket server is a separate Python script. To run it locally:

```bash
pip install websockets
python3 server.py
```

The server listens on **port 8765**. Both browser tabs must point to the same `WS_URL` (defaults to `ws://localhost:8765` when developing locally).

---

## Project Structure

```
tilestorm/
├── index.html       # The entire game — ~4100 lines
├── rfba-logo.png    # White frog silhouette on transparent background
├── server.py        # Python WebSocket server (asyncio + websockets)
└── .gitignore       # Ignores *.bak, __pycache__, node_modules, .env
```

### index.html

The whole game lives here — HTML, CSS, and JavaScript in one file. Sections are separated by prominent `═══` banner comments so you can jump between them quickly. ~4100 lines total.

### rfba-logo.png

The RFBA frog logo used in the red circle badge on the home screen. White frog silhouette on a transparent background.

### server.py

Python WebSocket server using the `asyncio` + `websockets` libraries. Manages multiplayer rooms identified by 6-digit codes. No database — all state is in-memory.

### .gitignore

Ignores: `*.bak`, `__pycache__/`, `node_modules/`, `.env`

---

## Code Navigation

Sections inside `index.html` appear in this order, each marked with a `═══` comment banner:

| # | Section | What's in it |
|---|---------|--------------|
| 1 | `<head>` | Google Fonts (Orbitron, Inter), meta tags |
| 2 | `<style>` | All CSS (~1600 lines). CSS variables defined at the top: `--red`, `--font-display`, `--font-body` |
| 3 | HTML body | Screen `<div>`s: `screen-title`, `screen-solo-setup`, `screen-game`, `screen-gameover`, `screen-duo-lobby` |
| 4 | FROG_SVGS | Inline SVG illustrations for each tier |
| 5 | TRIAL & MONETISATION SYSTEM | `initTrial`, `hasAccess`, `canPlay*` functions, upgrade modal logic |
| 6 | TIERS array | All 6 tier definitions — prices, perks, grid themes |
| 7 | TILE_PALETTES | Colour schemes per tier |
| 8 | GAME ENGINE | `calcLayout`, `drawGrid`, `startGame`, `placePiece`, `checkLines`, `updateScore` |
| 9 | SPECIAL BRICKS | Morph, meteor, and angel brick logic |
| 10 | DIFFICULTY SYSTEM | `DIFF_SETTINGS`, `setDifficulty`, `trySetDifficulty` |
| 11 | PREMIUM FEATURES | Legacy feature gate system (being replaced by the new `canPlay*` system) |
| 12 | SHOP | `buildShopUI`, `openShop`, `closePurchaseModal`, `confirmPurchase` |
| 13 | AUDIO | Web Audio API setup, `ensureAudio`, all sound-generation functions |
| 14 | SOLO SETUP | `openSoloSetup`, `updateLockIcons`, difficulty + challenge card handlers |
| 15 | CHALLENGE MODES | Frenzy, survival, colour-run logic — `initChallengeMode`, `stopChallengeMode` |
| 16 | DUO / MULTIPLAYER | WebSocket client, room creation/joining, duo game sync |
| 17 | Boot sequence | Last lines of the file (see below) |

### Boot sequence (last lines of index.html)

```js
calcLayout();
updateTierBadge();
loadStreak();
requestAnimationFrame(animateParticles);
initTrial();
updateTrialBanner();
updateLockIcons();
showScreen('screen-title');
```

**Order matters.** See [Critical Things NOT to Break](#critical-things-not-to-break).

---

## How to Edit & Deploy

### Editing

Edit `index.html` directly in any code editor. There is no compilation step.

### Deploying

Deployment requires **Perplexity Computer** (the AI that built the game) — it holds the `deploy_website` tool needed to push to the live host.

Deploy command (run inside Perplexity Computer):

```
deploy_website(
  project_path="/home/user/workspace/tilestorm",
  site_name="TileStorm",
  entry_point="index.html",
  should_validate=False
)
```

Always pass `should_validate=False`.

**Live URL:** https://www.perplexity.ai/computer/a/tilestorm-lNFITTzoTAmY.H9NxO57bQ

### After deploying, push to GitHub

```bash
git add -A && git commit -m "your description" && git push
```

---

## Key Functions to Know

| Function | What it does |
|----------|-------------|
| `showScreen(id)` | Switches the visible screen to the `<div>` with the given id |
| `startGame()` | Initialises a new game session |
| `initTrial()` | Called at boot. Sets `ts_trial_start` in localStorage if this is the user's first visit |
| `trialActive()` | Returns `true` if within the 7-day trial window |
| `hasAccess(tierId)` | Returns `true` if the user owns that tier or if the trial is still active |
| `canPlayMedium()` | Gate function — returns `true` if Medium difficulty is accessible |
| `canPlayHard()` | Gate function — returns `true` if Hard difficulty is accessible |
| `canPlayFrenzy()` | Gate function — returns `true` if Frenzy mode is accessible |
| `canPlaySurvival()` | Gate function — returns `true` if Survival mode is accessible |
| `canPlayColourRun()` | Gate function — returns `true` if Colour Run mode is accessible |
| `showUpgradeModal(reason)` | Displays the upgrade modal, passing a human-readable reason string |
| `checkAccessBeforeStart()` | Call before `startGame()` to block expired/unpaid users from starting |
| `confirmPurchase()` | **Simulated** purchase — saves tier to localStorage. Replace with real payment. |
| `updateTrialBanner()` | Updates the trial countdown pill on the home screen |
| `updateLockIcons()` | Shows or hides 🔒 on locked difficulty and challenge buttons |
| `isDuoSubscriber()` | **Currently hardcoded to `true`.** Replace with real payment check before launch. |

---

## Critical Things NOT to Break

1. **The rainbow 8-colour strip** at the top of every screen (`title-art-strips` div). It is a core visual identity element.

2. **The red circle badge** with the white RFBA frog logo on the home screen. It depends on `rfba-logo.png` being present at the project root.

3. **Trial banner visibility logic.** `updateTrialBanner()` reads `ts_trial_start` from localStorage. If that key is corrupted or absent (and `initTrial()` hasn't run yet), the banner will misbehave.

4. **Boot order.** The sequence at the bottom of `index.html` must stay in this order:
   ```
   initTrial()  →  updateTrialBanner()  →  showScreen()
   ```
   If `initTrial()` hasn't run before `updateTrialBanner()`, the trial banner will show incorrect data. If `showScreen()` runs before either, users may see a flash of wrong state.

---

## Before Going Live Checklist

- [ ] Replace `confirmPurchase()` with real Stripe or equivalent payment integration
- [ ] Revert `isDuoSubscriber()` to check real payment status (currently hardcoded `true`)
- [ ] Deploy `server.py` to a persistent host (e.g. Fly.io) and update `WS_URL` in `index.html`
- [ ] Add a GDPR consent banner
- [ ] Test on iOS Safari and Android Chrome (the primary mobile targets)
