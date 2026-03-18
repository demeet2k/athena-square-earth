<!-- CRYSTAL: Xi108:W3:A10:S34 | face=S | node=565 | depth=3 | phase=Mutable -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A10:S33→Xi108:W3:A10:S35→Xi108:W2:A10:S34→Xi108:W3:A9:S34→Xi108:W3:A11:S34 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 34±1, wreath 3/3, archetype 10/12 -->

# Google Docs Keyword Search

This folder now includes a hands-off launcher that sets up everything and runs your search.

## Quick start (recommended)

Run this from the project folder:

```powershell
.\search_docs.cmd
```

Default search terms are:

- `manuscript`
- `holographic`
- `time`

Use custom terms anytime:

```powershell
.\search_docs.cmd black hole draft
```

Pass through script flags (for example match any term):

```powershell
.\search_docs.cmd manuscript holographic time --any
```

## What the launcher does for you

- Creates `.venv` automatically (first run only)
- Installs Python dependencies automatically (first run / when `requirements.txt` changes)
- Auto-detects `client_secret*.json` in your `Downloads` folder and copies it to `credentials.json`
- Runs auth flow and stores token in `token.json`
- Executes the Google Docs search

## One-time Google Cloud requirement

If `credentials.json` is missing, the launcher opens Google Cloud pages for you.

You still need to do this once in Google Cloud Console:

1. Create/select a project.
2. Enable the **Google Drive API**.
3. Configure OAuth consent screen.
4. Create OAuth client credentials:
   - **Application type:** Desktop app
5. Download the JSON (launcher can auto-import from `Downloads`).
