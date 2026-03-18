<!-- CRYSTAL: Xi108:W3:A8:S26 | face=F | node=329 | depth=3 | phase=Mutable -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A8:S25→Xi108:W3:A8:S27→Xi108:W2:A8:S26→Xi108:W3:A7:S26→Xi108:W3:A9:S26 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 26±1, wreath 3/3, archetype 8/12 -->

# Google Docs Memory Sync Bootstrap

Date: 2026-03-09

## Objective

Unblock live Google Docs search for the Athena Agent workspace so Drive can become a searchable memory layer alongside the local and archive-backed corpus.

## Current Gate

- `credentials.json` is missing.
- `token.json` is missing.
- Verified against `C:\Users\dmitr\Documents\Athena Agent\Trading Bot\docs_search.py`.

## Expected File Locations

- OAuth client file:
  `C:\Users\dmitr\Documents\Athena Agent\Trading Bot\credentials.json`
- User token file:
  `C:\Users\dmitr\Documents\Athena Agent\Trading Bot\token.json`

## Required Google Cloud Setup

1. Open Google Cloud Console.
2. Create or select the project that should access your Google Drive.
3. Enable the Google Drive API.
4. Create an OAuth client for a Desktop App.
5. Download the client JSON.
6. Save it as:
   `C:\Users\dmitr\Documents\Athena Agent\Trading Bot\credentials.json`

## First Auth Run

From `C:\Users\dmitr\Documents\Athena Agent\Trading Bot`:

```powershell
.\.venv\Scripts\python.exe .\docs_search.py manuscript holographic time --max-results 25
```

Expected behavior:

- A browser window opens for Google auth.
- After consent, `token.json` is created automatically.
- The command returns matching Google Docs.

## JSON Probe

After first auth, use:

```powershell
.\.venv\Scripts\python.exe .\docs_search.py manuscript holographic time --max-results 10 --json
```

## Success Criteria

- `credentials.json` exists in `Trading Bot`.
- `token.json` exists in `Trading Bot`.
- `docs_search.py` returns at least one successful API response without OAuth errors.
- Live Docs can be treated as a new witness-bearing memory surface.

## Immediate Next Step After Unlock

Create a Docs manifest artifact that records:

- query
- document title
- modified time
- owner
- Google Docs URL
- local linkage to manuscript themes or runtime objectives
