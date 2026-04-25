# TileStorm — Platforms & Accounts Reference

> **Purpose:** Complete reference of every platform, account and service involved in TileStorm. Hand this to any developer so they know exactly where everything lives and what access they need.

---

## CODE & DEPLOYMENT

### GitHub
| Field | Value |
|---|---|
| URL | https://github.com/q2rnnyz2wv-create/tilestorm |
| Visibility | **Private** |
| Account | `q2rnnyz2wv-create` |
| Contains | All source code, including `index.html`, `server.py` |

**Access:** Owner must add collaborators via **GitHub Settings → Collaborators**. Developers need at least *Write* access to push branches; *Admin* access to manage settings.

---

### Perplexity Computer (Deployment Tool)
| Field | Value |
|---|---|
| URL | https://perplexity.ai |
| Purpose | Used to deploy the game via the `deploy_website` tool |
| Hosting | Game is served from Perplexity's S3 CDN automatically on deploy |
| Live game URL | https://www.perplexity.ai/computer/a/tilestorm-lNFITTzoTAmY.H9NxO57bQ |
| Asset ID | `94d1484d-3ce8-4c09-98f8-7f4dc4ee7b6d` |

**Access:** Deployment is done through the Perplexity UI. Use the **Share** button in the Perplexity Computer interface to make the deployed game publicly accessible. No separate CDN login is required — hosting is fully automatic.

---

## GAME HOSTING (STATIC)

### Perplexity S3 CDN
| Field | Value |
|---|---|
| Provider | Perplexity (S3-backed CDN) |
| Setup required | None — automatic when deploying via Perplexity Computer |
| Separate login | Not required |

The static game files (`index.html`, assets) are served from this CDN every time a deployment is triggered through Perplexity Computer. No manual S3 configuration needed.

---

## MULTIPLAYER SERVER — ⚠️ NOT YET LIVE

> **Current status:** The WebSocket server is **not running**. The `WS_URL` in `index.html` is hardcoded to an **expired Cloudflare tunnel**. **Duo multiplayer will not work** until a permanent server is deployed and `WS_URL` is updated.

### Option A — Fly.io (Recommended)
| Field | Value |
|---|---|
| URL | https://fly.io |
| Account status | Needs setting up |
| What to deploy | `server.py` from the GitHub repo |
| Result | Permanent `wss://` URL |
| Cost | ~£5–20/month (covers multiple apps) |

Fly.io provides persistent, scalable hosting with a stable WebSocket URL. Suitable for production. The same account can host the GCSE game server.

### Option B — Railway (Alternative)
| Field | Value |
|---|---|
| URL | https://railway.app |
| Account status | Needs setting up |
| Advantage | Simpler to get started, free tier available |
| Limitation | Lower scale ceiling than Fly.io |

Good for rapid prototyping or initial launch. Migrate to Fly.io if traffic grows.

### After deploying either option:
1. Copy the `wss://` URL provided by the platform.
2. Update `WS_URL` in `index.html` in the GitHub repo.
3. Redeploy via Perplexity Computer.

---

## PAYMENT — ⚠️ NOT YET INTEGRATED

> **Current status:** Purchases are **simulated** in the current build. `isDuoSubscriber()` is hardcoded to `true`. No real money can be collected safely until this is replaced.

### Recommended: Stripe (Web Payments)
| Field | Value |
|---|---|
| URL | https://stripe.com |
| Best for | Web-based payments (subscriptions, one-time purchases) |
| Account status | Not yet set up |

### Alternative: RevenueCat (Native Apps)
| Field | Value |
|---|---|
| URL | https://revenuecat.com |
| Best for | In-app purchases on iOS/Android native apps |
| Account status | Not yet set up |

### VAT
- Owner is **not yet VAT registered**.
- No VAT is charged in the current pricing.
- Must register when revenue approaches the UK threshold: **£90,000/year**.

---

## BRAND & WEBSITE

### RFBA Website
| Field | Value |
|---|---|
| URL | https://redfrogblackart.com |
| Purpose | Owner's art business — TileStorm to be published here |
| Platform | Wix / GoDaddy (inferred from font CDN URLs) |
| Managed by | Owner independently |

### Brand Identity
| Element | Value |
|---|---|
| Primary red | `#CC1212` |
| Theme colour | `#f20505` |
| Black | `#080808` |
| White | `#ffffff` |
| Heading font | Fjalla One |
| Body font | Source Sans Pro |

These match the RFBA website and must be consistent across the game, marketing materials and any app store listings.

---

## APP STORES — ⚠️ NOT YET SUBMITTED

> **Current status:** TileStorm is a **web app**. For native app store submission, the codebase must be wrapped using **Capacitor** or **React Native** first. See the launch checklist PDF (`tilestorm_launch_checklist`) for details.

### Google Play Store
| Field | Value |
|---|---|
| Console URL | https://play.google.com/console |
| Account required | Google account |
| One-time developer fee | **$25** |
| Wrapping needed | Capacitor (or React Native) |
| Status | Not submitted |

### Apple App Store
| Field | Value |
|---|---|
| Console URL | https://appstoreconnect.apple.com |
| Account required | Apple Developer account |
| Annual fee | **$99/year** |
| Wrapping needed | Capacitor (or React Native) |
| Status | Not submitted |

---

## MARKETING & SOCIAL — BACKLOG

| Item | Status |
|---|---|
| Social media teasers with British voiceover | **In backlog** — not yet created |
| App store listing copy | **Ready** — see `/home/user/workspace/app_store_listing.md` |
| Game name decision | **Pending** — CROAKDOWN recommended as alternative; owner has not yet decided |

---

## DOCUMENTS & FILES

| Document | Location |
|---|---|
| All project docs | `/home/user/workspace/docs/` |
| Launch checklist | Previously shared as `tilestorm_launch_checklist` (PDF) |
| App store guide | Previously shared as `tilestorm_appstore_guide` (PDF) |
| Name research | Previously shared as `tilestorm_name_research` (PDF) |
| UI proposal | Previously shared as `tilestorm_ui_proposal` (PPTX) |
| App store listing copy | `/home/user/workspace/app_store_listing.md` |
| Platforms & accounts (this doc) | `/home/user/workspace/docs/03_platforms_and_accounts.md` |
| Outstanding actions | `/home/user/workspace/docs/04_outstanding_actions.md` |

---

*Last updated: based on full TileStorm project chat history.*

---

## 📧 Account Email Reference

| Purpose | Email to Use |
|---------|-------------|
| Primary (all platforms) | info@redfrogblackart.com |
| Backup / account recovery | kzitova@windowslive.com |
| GitHub account | info@redfrogblackart.com |
| Fly.io account | info@redfrogblackart.com |
| Apple Developer account | info@redfrogblackart.com |
| Google Play account | info@redfrogblackart.com (needs Google account) |
| Stripe / payments | info@redfrogblackart.com |

**Note on Google:** Google Play requires a Google account. Create one at google.com using info@redfrogblackart.com as the email — takes 2 minutes and means all your developer accounts are under one brand identity.

**Note on recovery:** Set kzitova@windowslive.com as the backup/recovery email on every platform so you can always regain access if needed.
