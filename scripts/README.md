# Festival Image Generation Scripts

Local Python tooling that calls the Gemini API (Nano Banana / `gemini-2.5-flash-image`) to generate the 9 festival images for Sacred Japan. Returned PNG bytes are converted to JPEG at quality 92 before saving.

Outputs land in `../images/festival-{name}.jpg` and are picked up automatically by the existing festival cards in `index.html`.

## One-time setup

From `C:\Users\teruh\sacred-japan\scripts\` (PowerShell):

```powershell
# 1. Create a venv (keeps deps isolated from system Python)
py -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env from the template, then paste your key
copy .env.example .env
notepad .env
```

Get a fresh API key at https://aistudio.google.com/app/apikey — restrict it to **Generative Language API** only.

`.env` is gitignored. Never commit it.

## Run

```powershell
# Activate venv if not already active
.\.venv\Scripts\Activate.ps1

# Generate all 9 festivals
py generate_festivals.py

# Or just specific ones
py generate_festivals.py gion sanja nebuta

# Force overwrite without prompting
py generate_festivals.py --force
```

Valid festival names: `gion sanja tenjin kanda aoi jidai nebuta awa yosakoi`

## After generation

```powershell
cd ..
git add images/festival-*.jpg
git commit -m "Add festival images"
git push origin main
```

GitHub Pages will redeploy in 1–2 minutes; refresh `https://sacred-japan.net/#festivals`.

## Troubleshooting

- **`GEMINI_API_KEY not set`** → `.env` missing or empty. Copy from `.env.example`.
- **`safety-filter block`** → Gemini's filter rejected the prompt. Edit the offending prompt in `generate_festivals.py` (e.g. soften "fierce warrior" wording for Nebuta) and rerun just that one: `py generate_festivals.py nebuta --force`.
- **`PERMISSION_DENIED` / `API key not valid`** → Key was revoked or doesn't have Generative Language API enabled. Re-issue and update `.env`.
- **`RESOURCE_EXHAUSTED`** → Quota hit. Check billing / quota in Google AI Studio.
- **Want a different model** → Change the `MODEL` constant in `generate_festivals.py` (e.g. `"imagen-4.0-generate-001"` for Imagen 4; note Imagen uses a different endpoint and the script's call site would need adjustment).
