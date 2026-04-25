# 🚀 Fly.io Server Setup — Step by Step

This guide sets up the TileStorm multiplayer WebSocket server on Fly.io.  
**Written for non-technical users — every step is spelled out.**

---

## What This Does
Fly.io will host `server.py` permanently so Duo mode works for real players anywhere in the world. Cost: approximately £5–20/month (covers TileStorm + any other RFBA apps).

---

## Step 1 — Create Your Fly.io Account
1. Go to **[fly.io](https://fly.io)**
2. Click **"Get Started"** (top right)
3. Sign up with your email — use the same email you use for everything RFBA
4. Verify your email
5. Add a payment card (you won't be charged until you deploy — there's a free allowance)
6. **Write down / save your Fly.io email** — add it to the platforms doc

---

## Step 2 — Install the Fly.io Command Line Tool (flyctl)

**On Mac:**
```bash
brew install flyctl
```
**On Windows:**  
Download installer from: https://fly.io/docs/flyctl/install/

**On any computer via terminal:**
```bash
curl -L https://fly.io/install.sh | sh
```

---

## Step 3 — Log In
Open Terminal (Mac) or Command Prompt (Windows) and type:
```bash
fly auth login
```
A browser window opens — log in with your Fly.io account. Come back to the terminal when done.

---

## Step 4 — Deploy the TileStorm Server

In your terminal, navigate to your TileStorm folder:
```bash
cd path/to/tilestorm
fly launch
```

When it asks questions:
- **App name:** `tilestorm-ws` (or whatever you like)
- **Region:** Choose **London (lhr)** — closest to your UK players
- **Would you like to set up a Postgresql database?** → **No**
- **Would you like to set up an Upstash Redis database?** → **No**
- **Deploy now?** → **Yes**

Wait 2–3 minutes. At the end you'll see something like:
```
Visit your newly deployed app at https://tilestorm-ws.fly.dev
```

**Copy that URL** — you'll need it in the next step.

---

## Step 5 — Update the Game with the New Server URL

Tell Perplexity Computer (in the TileStorm conversation):

> "The Fly.io server is live at wss://tilestorm-ws.fly.dev — please update the WS_URL in the game and redeploy"

That's it. The AI does the rest.

---

## Step 6 — Verify It's Working
1. Open the game at: https://www.perplexity.ai/computer/a/tilestorm-lNFITTzoTAmY.H9NxO57bQ
2. Tap **DUO PLAY**
3. Tap **CREATE ROOM** — you should see a 4-letter room code appear
4. On another device/browser, tap **JOIN ROOM** and enter the code
5. If both players connect — it's working ✅

---

## Ongoing Management

**Check your server is running:**
```bash
fly status --app tilestorm-ws
```

**View logs if something goes wrong:**
```bash
fly logs --app tilestorm-ws
```

**Redeploy after code changes:**
```bash
fly deploy --app tilestorm-ws
```

**Monthly cost:** Check at [fly.io/dashboard](https://fly.io/dashboard) → Billing

---

## Adding the GCSE Game to the Same Account
Once TileStorm server is live, open the GCSE game conversation in Perplexity and say:
> "I have a Fly.io account — email is [your email]. Please set up the GCSE game server there too, same as TileStorm."

The AI will handle everything. Both apps share the same account — one bill, one dashboard.

---

## 🆘 If You Get Stuck
- Fly.io live chat support: [fly.io/docs](https://fly.io/docs)
- Or tell Perplexity Computer: "Fly.io setup failed, here's the error: [paste error]"

