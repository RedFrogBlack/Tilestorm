# 🐸 TileStorm — RedFrogBlackArt

**A tile-placement puzzle game by RedFrogBlackArt**  
*"Unleash your playful side"*

---

## 🎮 Play the Game
**Live URL:** https://www.perplexity.ai/computer/a/tilestorm-lNFITTzoTAmY.H9NxO57bQ  
*(Share via the Perplexity UI Share button to make it public)*

---

## 📁 What's in This Repo

| File | Purpose |
|------|---------|
| `index.html` | The entire game — HTML, CSS, and JavaScript (~4100 lines) |
| `rfba-logo.png` | RFBA white frog logo (transparent background) |
| `server.py` | WebSocket server for Duo multiplayer mode |
| `docs/` | All documentation — start here if you're a new developer |

---

## 📚 Documentation (Start Here)

All docs are in the `/docs` folder:

| Doc | What it covers |
|-----|---------------|
| [01 — Architecture](docs/01_architecture.md) | System overview, how everything connects, security, known issues |
| [02 — Features & Tiers](docs/02_features_and_tiers.md) | Every game feature, tier pricing, buttons explained |
| [03 — Platforms & Accounts](docs/03_platforms_and_accounts.md) | Every service/platform used, where to log in |
| [04 — Outstanding Actions](docs/04_outstanding_actions.md) | Everything still to do, in priority order |
| [05 — Developer Handover](docs/05_developer_handover.md) | How to edit, run, and deploy the game |
| [06 — Data Flows](docs/06_data_flows.md) | localStorage, trial system, WebSocket protocol |

---

## ⚡ Quick Start (for developers)

```bash
git clone https://github.com/q2rnnyz2wv-create/tilestorm
cd tilestorm
# Open index.html in your browser — no build step needed
# For duo multiplayer server:
pip install websockets
python3 server.py
```

---

## 🚨 Critical Before Going Live

- [ ] WebSocket server needs permanent hosting (Fly.io recommended)
- [ ] `isDuoSubscriber()` is hardcoded `true` — must revert before launch
- [ ] Real payment integration needed (Stripe/RevenueCat) — purchases are currently simulated
- [ ] GDPR consent banner required for UK users

---

## 🎨 Brand

- **Studio:** RedFrogBlackArt — [redfrogblackart.com](https://redfrogblackart.com)
- **Brand Red:** `#CC1212`
- **Background:** `#080808`
- **Fonts:** Orbitron (game display) · Fjalla One (brand) · Source Sans Pro (body)
- **Tagline:** *Unleash your playful side*

---

*Built with Perplexity Computer. For support or to continue development, open the TileStorm conversation in Perplexity.*
