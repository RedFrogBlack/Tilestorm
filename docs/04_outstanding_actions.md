# TileStorm — Outstanding Actions

> **Purpose:** Everything discussed but not yet completed, ordered by priority. Work through this checklist before launch and beyond.

---

## 🔴 CRITICAL — Must complete before taking real money

These items are not optional. The game must not accept real payments until all of these are resolved.

- [ ] **Set up permanent WebSocket server** (Fly.io or Railway) and update `WS_URL` in `index.html`
  - Current `WS_URL` points to an expired Cloudflare tunnel — duo multiplayer is broken
  - See `03_platforms_and_accounts.md` for Fly.io vs Railway comparison

- [ ] **Revert `isDuoSubscriber()` from hardcoded `true` to a real payment check**
  - Currently all users are treated as paid subscribers regardless of purchase

- [ ] **Integrate real payment processor** (Stripe for web, or RevenueCat for native apps)
  - Purchases are entirely simulated in the current build

- [ ] **Add server-side ownership verification**
  - `localStorage` can be spoofed by any user — ownership must be verified server-side

- [ ] **Add GDPR cookie consent banner**
  - Legally required in the UK for any web service that stores data or uses analytics

- [ ] **Test all payment flows end to end before going live**
  - Cover: successful purchase, failed card, subscription cancel, restore purchases

---

## 🟠 HIGH PRIORITY — Complete before launch

- [ ] **Decide on game name: TILESTORM or CROAKDOWN (or another)?**
  - Name research PDF shared (`tilestorm_name_research`) — owner has not yet decided
  - Decision gates: app store listings, social media handles, any press/marketing

- [ ] **Submit to Google Play Store**
  - Requires: $25 one-time developer fee, Google Play Console account
  - Requires: wrapping the web app in Capacitor or React Native first

- [ ] **Submit to Apple App Store**
  - Requires: $99/year Apple Developer account, App Store Connect account
  - Requires: wrapping the web app in Capacitor or React Native first

- [ ] **Publish game on RFBA website** (https://redfrogblackart.com)
  - Game should be accessible or linked from the owner's existing art site

- [ ] **Set up social media presence** for TileStorm (or under the RFBA brand)
  - Secure handles early — especially if the game name changes

- [ ] **Monitor VAT threshold**
  - Register for VAT when revenue is approaching £90,000/year (UK threshold)
  - No VAT is charged in the current build

---

## 🟡 MEDIUM PRIORITY — Marketing

- [ ] **Create social media teasers**
  - Discussed: short videos with British accent voiceover
  - Status: explicitly requested and placed **in backlog** — not yet created

- [ ] **Write and schedule launch posts** for social media

- [ ] **Set up app store screenshots and preview videos**
  - Required for both Google Play and Apple App Store submissions

- [ ] **Submit app store listing copy**
  - Copy is **ready** at `/home/user/workspace/app_store_listing.md`
  - Just needs uploading to Google Play Console / App Store Connect

---

## 🟡 MEDIUM PRIORITY — Game improvements discussed but not yet built

- [ ] **Mobile icon/button size audit**
  - Some buttons may still be below Apple's minimum 44×44px tap target requirement

- [ ] **Progressive unlock UI**
  - Show Shop icon only after Level 3 is reached
  - Show challenge modes only after the player's first completed game

- [ ] **Reduce in-game top bar**
  - Currently shows: Score / Best / Level / Lines
  - Proposed: show Score + Level only to reduce visual clutter

- [ ] **Power-up button visibility**
  - Only show the power-up button when a power-up has actually been earned
  - Currently always visible regardless of earned state

- [ ] **ADHD accessibility mode**
  - See ADHD audit document for full spec (previously shared)

---

## 🔵 BACKLOG — Future features

- [ ] Social media video teasers with British voiceover *(explicitly requested — in backlog)*
- [ ] Global leaderboards
- [ ] Friends leaderboards
- [ ] Daily challenges
- [ ] Push notifications for streak reminders
- [ ] Migrate WebSocket server from Railway to Fly.io if traffic warrants it
- [ ] GCSE game — also needs deploying to Fly.io for multiplayer/persistence

---

## ⚙️ INFRASTRUCTURE

- [ ] **Set up Fly.io account** and deploy `server.py` for TileStorm duo multiplayer
- [ ] **Consider deploying GCSE game server** to the same Fly.io account
- [ ] **Set up Cloudflare** in front of all apps (free DDoS protection + CDN)
- [ ] **Set up monitoring/alerts** — e.g. UptimeRobot (free tier) so owner is notified if the WebSocket server goes down

---

*Last updated: based on full TileStorm project chat history.*

---

## 🌐 Domain & Corporate Structure

### Domains You Already Own
| Domain | Registrar | Notes |
|--------|-----------|-------|
| redfrogblack.com | GoDaddy | Corporate hub — site to be built |
| redfrogblack.co.uk | GoDaddy | **Renews October 2026 — set auto-renew!** |
| redfrogblackart.com | — | Art + clothing — stays as-is |

### Domains to Buy This Week
- [ ] Buy **croakdown.com** at Namecheap (~£10/yr) — use info@redfrogblackart.com
- [ ] Buy **croakdown.co.uk** at Namecheap (~£8/yr) — same account
- [ ] Set auto-renew on redfrogblack.co.uk in GoDaddy (expires Oct 2026)

### Corporate Site (redfrogblack.com) — Future Project
- [ ] Build corporate hub listing all RFBA businesses:
  - RedFrogBlackArt (art + clothing) → redfrogblackart.com
  - CROAKDOWN (game) → croakdown.com
  - GCSE App → own domain TBD
  - We Work as a Team → own domain TBD
  - Future products...

### Email Structure
- Primary for all platforms: **info@redfrogblackart.com**
- Backup/recovery: **kzitova@windowslive.com**
- Consider: info@redfrogblack.com for corporate communications (once site is built)
