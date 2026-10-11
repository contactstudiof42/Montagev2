# Journal Resolve — P3-sony-linkbuds-agent

_Base « TEST IA », Resolve Studio 21.1.1. Chaque appel MCP (`run_script` sauf mention), son résultat et son contrôle. Gestes déjà validés : `labo/mcp/journal-2026-10-11.md`._

| # | Heure | Geste | Appel | Résultat | Contrôle |
|---|---|---|---|---|---|
| 1 | 13:2x | Projet | `pm.CreateProject("P3-sony-linkbuds-agent")` ; `SetSetting` 1080 / 1920 / 25 | créé ; `timelinePlaybackFrameRate` refusé (sans effet ici) | `GetName()` |
| 2 | | Import | dossiers RUSH, SON, MUSIQUE, ASSET, SFX ; `ImportMedia([".../SONY copy/RUSH/"])` (dossier entier), musique, plan de fin, logo | 252 rushes, 1 musique, 2 assets ; sources non modifiées (import = référence) | comptes |
