# 07 — ADHD Accessibility Audit
**TileStorm | Game Design Documentation**

---

## Overview

This document audits TileStorm through the lens of ADHD accessibility — looking at what the game already does well, where it falls short, and what to build next. The goal is to make TileStorm a game that players with ADHD can genuinely enjoy without friction, frustration, or losing the thread.

ADHD affects roughly 5–10% of adults. For games, this means players who thrive on immediate feedback, clear short-term goals, and low-friction starts — and who can really struggle with visual clutter, open-ended sessions, or buried controls. The good news: TileStorm's core design is already well-suited to this audience. There are just a few gaps to close.

---

## What TileStorm Already Gets Right

These are genuine strengths. No changes needed — just worth knowing they're working in your favour.

| Strength | Why It Helps ADHD Players |
|---|---|
| **Bright, high-contrast RFBA colour palette** | High visual contrast reduces cognitive effort — the brain tracks pieces without having to work for it |
| **Clear visual feedback on piece placement** | Immediate confirmation that an action worked — essential for the ADHD reward loop |
| **Bubble-style popups (non-blocking)** | Feedback lands without interrupting the game flow. This is a smart design call |
| **Short sessions — especially Frenzy 25s** | ADHD players often can't commit to long sessions. A natural 25-second game is a gift |
| **Sound effects and audio feedback** | Multi-sensory feedback reinforces actions and keeps attention engaged |
| **Streak system** | Daily structure and motivation — gives the game a "reason to return" beyond just playing |
| **One-finger / one-click gameplay** | Low mechanical complexity means attention can go to the puzzle, not the controls |
| **Large, colourful tiles** | Easy to track visually — no hunting for small targets |
| **Challenge modes (Frenzy, Survival)** | Time pressure and stakes provide the urgency that ADHD brains often need to stay engaged |
| **Score counter** | A constant, visible feedback loop. Numbers going up is inherently motivating |

**Summary:** TileStorm's core gameplay loop — place tile, get feedback, see score go up — is genuinely ADHD-friendly. The Frenzy mode especially is close to ideal.

---

## Current Gaps

These are the areas where ADHD players are most likely to disengage, feel overwhelmed, or not return.

**1. Standard mode has no time limit**
Without a clock or goal, Standard mode can feel directionless. ADHD players may place a few tiles and drift — there's no urgency pulling them back into focus.

**2. Too many stats in the top bar**
Score / Best / Level / Lines — four data points competing for attention simultaneously. For ADHD players, this creates low-level cognitive noise. Only two of these are needed in the moment.

**3. Shop decision fatigue**
Many options presented at once without a clear recommendation or "best for you" path. ADHD players tend to either get stuck choosing or skip the shop entirely.

**4. Home screen has too many competing elements**
Trial banner, tier badge, streak counter, and multiple buttons all vie for attention at once. There's no clear "just play" path.

**5. No focus mode or reduced-distraction option**
Players who want a clean, calm experience have no way to strip back the UI.

**6. Sound toggle is buried**
If a player wants to toggle sound, they have to find it. This is a small friction point, but small friction points matter for ADHD.

**7. No notification or reminder system**
The streak system is motivating — but only if players remember to come back. There's nothing nudging them.

---

## Recommended Improvements

Each improvement is listed with what it is, why it helps ADHD players specifically, build difficulty, and priority.

---

### 1. "⚡ BEST FOR FOCUS" Tag on Frenzy Mode
**Priority: High | Difficulty: Easy**

**What it is:** A small subtle label — "⚡ BEST FOR FOCUS" — on the Frenzy challenge card on the mode-select screen. Not a popup, not a tooltip. Just a quiet badge that's always there.

**Why it helps:** ADHD players often find decision-making hard, especially when options look equally valid. A gentle recommendation removes the choice overhead and points them toward the mode that's genuinely best-suited to them. Frenzy's time-boxed structure is exactly what helps ADHD brains engage: urgency, a clear end point, and a score to beat.

**How to build:** Add a small styled `<span>` or CSS badge to the Frenzy card. One line of HTML, a few lines of CSS. No logic needed.

---

### 2. Reduce Top Bar to Score + Level Only
**Priority: High | Difficulty: Easy**

**What it is:** During gameplay, the top bar shows only Score and Level. Best and Lines are hidden (or moved to the post-game summary screen where they're actually useful).

**Why it helps:** Fewer data points in peripheral vision means less cognitive load during play. ADHD players aren't ignoring the extra stats — their brains are processing them even when not needed, which quietly drains focus. Score tells you how you're doing right now. Level tells you where you are. That's all you need mid-game.

**How to build:** CSS `display: none` on the Best and Lines elements during active gameplay. Show them on the results screen. This is already on the outstanding actions list.

---

### 3. "Focus Mode" Toggle
**Priority: High | Difficulty: Medium**

**What it is:** A single tap/click toggle — accessible from the home screen and ideally from in-game — that hides the streak counter, tier badge, and trial banner. In Focus Mode, the player sees: the game, the score, and nothing else competing for attention.

**Why it helps:** ADHD players are often hyperaware of visual elements even when trying to ignore them. The trial banner, tier badge, and streak widget are all legitimately useful — but not all at once, and not when someone is trying to focus. A Focus Mode gives players agency over their environment without losing any features permanently.

**How to build:**
- Add a `focusMode` boolean to app state (localStorage or sessionStorage is fine)
- Toggle it with a small button (e.g., a 🎯 or "FOCUS" label in the corner of the home screen)
- Conditionally render the streak widget, tier badge, and trial banner based on this flag
- Persist the preference so it survives app restarts

This is a medium lift but has high impact. Well worth it.

---

### 4. Haptic Feedback on Line Clear
**Priority: Medium | Difficulty: Easy**

**What it is:** A short vibration pulse when a player clears a line, using the browser's `navigator.vibrate()` API on mobile devices.

**Why it helps:** Multi-sensory feedback reinforces the moment of reward. For ADHD players, the more senses that register "that worked", the stronger the positive signal. A line clear already triggers a visual animation and a sound — adding a physical pulse completes the loop. It's also satisfying in a way that's hard to explain until you feel it.

**How to build:**
```js
if (navigator.vibrate) navigator.vibrate(80);
```
One line of code, called at the point where a line clear is detected. Optionally add a user preference to disable it (alongside the sound toggle).

---

### 5. Sound Toggle on Home Screen
**Priority: Medium | Difficulty: Easy**

**What it is:** A small 🔊 / 🔇 icon button, top-right of the home screen, that toggles game audio on and off. Visible immediately without navigating to settings.

**Why it helps:** ADHD players often play in contexts where sound isn't appropriate — commuting, in a meeting, at 2am. If they can't immediately silence the game, they'll close it. Low friction to start playing is essential, and that includes being able to quickly mute. Buried settings controls are a quiet exit trigger.

**How to build:**
- Move (or duplicate) the sound toggle to the home screen header
- Use the existing sound state — this is a UI placement change, not new logic
- Small icon button, 40x40px minimum tap target, persists via localStorage

---

### 6. Colour-Blind Friendly Mode (Shape Indicators on Tiles)
**Priority: Medium | Difficulty: Medium**

**What it is:** An optional mode that adds a small shape symbol to each tile — ● for one colour family, ▲ for another, ■ for another, etc. — so that colour is no longer the only differentiator between tile types.

**Why it helps ADHD players specifically:** ADHD and colour vision deficiency co-occur at above-average rates. More broadly, shape redundancy helps any player track tile types without relying solely on colour memory — reducing the amount of information the brain has to hold in working memory at once. It's also just good accessible design.

**How to build:**
- Define a shape mapping for each tile colour in the RFBA palette
- Render a small SVG symbol in the centre (or corner) of each tile when this mode is active
- Add a toggle in settings (and optionally on the home screen)
- Keep symbols small enough not to distract when colour alone is sufficient

---

### 7. "Quick Start" Button
**Priority: Low | Difficulty: Easy**

**What it is:** A prominent button on the home screen — "QUICK START" or "▶ PLAY" — that bypasses any mode-selection screen and immediately starts a game using the player's last-used settings.

**Why it helps:** One of the most common ADHD exit points is the gap between "I want to play" and "the game has started". Every tap that isn't gameplay is a moment where attention can wander. Quick Start collapses the friction to near zero — tap once, you're playing.

**How to build:**
- Store last-used mode/settings in localStorage
- Add a single button to the home screen that reads those settings and calls the game-start function directly
- Default to Frenzy 25s for new users (pairs well with improvement #1)

---

## Developer Note: ADHD Design Principles for Games

If you're implementing any of the above — or making future design decisions — these principles are worth keeping in mind. They apply broadly to good game design, but ADHD players feel their absence much more acutely.

**Short feedback loops**
The time between action and reward should be as short as possible. In TileStorm, this is already good — placing a tile gives instant visual feedback. Protect this. Don't add animations or transitions that delay the reward signal.

**Clear goals at all times**
Players should always know what they're trying to do right now. In Frenzy mode, this is clear: survive, score, beat the timer. In Standard mode, it's fuzzier. Where possible, surface a micro-goal — "clear a line", "beat your best", "reach Level 5" — even if the player didn't set it.

**Immediate reward**
Positive feedback should feel good and happen immediately. Sound + visual flash + haptic = three reward channels firing at once. More channels = stronger signal = more engagement. This is why improvement #4 (haptics) is worth one line of code.

**Low friction to start**
The number of taps between "I want to play" and "I am playing" should be as close to one as possible. Quick Start (#7) addresses this directly. So does the sound toggle on the home screen (#5) — removing a reason to pause before starting.

**Ability to stop and resume cleanly**
ADHD players are often interrupted — by a thought, a notification, or just losing the thread. Games that punish interruption (no pause, no save state) lose these players fast. If TileStorm doesn't already support pausing mid-game and resuming cleanly, this is worth adding. It doesn't need to be complex — even a simple "tap to resume" screen is enough.

---

## Summary Table

| # | Improvement | Priority | Difficulty | ADHD Benefit |
|---|---|---|---|---|
| 1 | "⚡ BEST FOR FOCUS" tag on Frenzy | High | Easy | Removes decision fatigue, guides players to the best mode |
| 2 | Reduce top bar to Score + Level | High | Easy | Cuts visual noise during gameplay |
| 3 | Focus Mode toggle | High | Medium | Strips distractions on demand |
| 4 | Haptic feedback on line clear | Medium | Easy | Adds sensory reward channel |
| 5 | Sound toggle on home screen | Medium | Easy | Removes a friction point before starting |
| 6 | Colour-blind / shape mode | Medium | Medium | Reduces working memory load, broadens accessibility |
| 7 | Quick Start button | Low | Easy | Minimises taps-to-gameplay |

---

*Document version: 1.0 | Part of the TileStorm design documentation series*
