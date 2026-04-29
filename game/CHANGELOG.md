# Croakdown Changelog

## v3 Premium Polish — 29 Apr 2026

### Renamed
- POISON DART → **FOG THE FROG** in every visible UI string (HTP tier card, TIERS array, survival event banner, TIER_META subtitle, upgrade modal, settings tier list, glitch overlay, home tier card border). The internal `poisondart` product ID and function names are preserved so receipts, IAP plumbing, and pack-unlock logic remain valid.
- Pack accent for Fog the Frog switched from harsh red `#CC1212` to thematic fog-green `#6B8F71`.
- VENOM ☠️ power-up icon kept (gameplay mechanic, not a pack name).

### City Pack added as 5th Solo pack
- New `.pack-card.city` accent `#4A9EFF` with animated skyline-drift background.
- Added markup at solo-setup with id `gtc-citypack`, fully wired through `buildSoloSetupCards`, `showPackUnlockedBanner`, and play-button click handler.
- Plays through `startCityPackGame(0)` using the existing 10-city tour (LONDON, NEW YORK, PARIS, TOKYO, DUBAI, SYDNEY, CHICAGO, HONG KONG, MOSCOW, MIAMI).
- Home Solo Play subtitle now reads "5 game packs" (was 4).

### Solo cards — premium v3 visual layer
- Each card has a per-tier animated tinted background (Tadpole ripple, Tree Frog frenzy pulse, Fog drift, Golden shimmer, City Pack skyline drift).
- Card now uses glassy raised look with 1px white border, gradient inner fill, larger 56×56 emoji block, name with accent dot prefix, right-side state slot.
- Three states styled distinctly:
  - **Trial** → green "FREE 7 DAYS" pill + "then £0.99/yr" sub-text
  - **Owned** → green "OWNED ✓" pill, accent border-glow inset
  - **Locked** → big accent-coloured price (e.g. `£1.99/yr`) with lock icon
- Whole card is tappable (legacy ▶ PLAY button hidden — was unreliable behind a `hidden` attr).
- 7-Day Free Trial chip in the header is now driven by `userOnTrial` state and only shows during the trial.

### Duo lobby polish
- All three game cards (Pond Battle, Shake the Frog, Frog Swap) get the same premium glass treatment with mode-tinted left-side accent gradient.
- 54×54 glass emoji block + cleaner SELECT chip.
- Type rhythm: 15px name, 12.5px description.

### In-game HUD — premium polish
- Per-mode CSS variables (`--mode-accent`, `--mode-accent-soft`, `--mode-accent-glow`) automatically applied to the body via `_syncBodyMode()` based on the active mode (standard / frenzy / survival / colourrun / citypack / duo).
- Top bar dark glass with mode-tinted underglow + scanline strip.
- Stat pills bump-animate on score and level changes (combo, mode-gradient).
- Event banner (challenge-hud) reskinned: glass with backdrop blur, mode-tinted gradient + glow, rounded corners, 8px outset margin (was full-bleed harsh red bar).
- Mid-tier badge: mode-outlined chip with level-up pulse ring on level-up.
- Full-screen "LEVEL UP · 2" ribbon fly-in on every level increment, suppressed on initial paint.
- `_updateMidZone()` now refreshed every `updateUI` tick so the bottom tier badge accurately reflects active challenge mode.

### Backgrounds — distinct & premium
- Tadpole: gentle green ripple
- Tree Frog: frenzy 1.6s timer pulse
- Fog the Frog: drifting cloud layers (14s)
- Golden Frog: linear gold shimmer (6s)
- City Pack: skyline silhouette + slow sky drift (12s)

### Verified end-to-end
- All 5 Solo packs boot from Home → Solo → tap card → game starts.
- Duo lobby shows three game cards + Duo magic powers + create/join/vs-Frog panels.
- HOW TO PLAY overlay opens cleanly from Home.
- 414×896 mobile viewport audit screenshots: trial state, owned state, locked state, all in-game modes.

### Hard rules respected
- `poisondart` product ID unchanged.
- `.screen.hidden { display: none !important; }` rule kept.
- Brand: Red Frog Black Limited (UK) · info@redfrogblackart.com · Klara
- Bundle: com.redfrogblackart.croakdown · Capacitor 8.3.1 + @capgo/native-purchases
- IAP product IDs locked (Tadpole/TreeFrog/Fog/Golden/CityPack/Duo/SPARK/SURGE/STORM)

### Still on the master roadmap (next iterations)
- Remove legacy `upgrade-overlay` and `purchase-overlay` once the new pack-unlock banner flow is fully canonical.
- Capacitor IAP wrapper (web fallback already works).
- Full copy rewrite + diff document for Klara review.
- Full responsive audit at 375 / 414 / 768 px.
