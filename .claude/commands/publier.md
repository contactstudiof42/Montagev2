---
description: Publier les skills du robot vers le cabinet (Post-prod clients), sur le feu vert de Diego
---
Publie mon savoir vers le cabinet `/Users/diego/Post-prod clients/` (voir `CLAUDE.md`, section « Le cabinet »).

1. `git status` : si des skills ou l'agent DA ont des modifications non commitées, commit et push d'abord. On ne publie que du savoir commité.
2. Lis la dernière ligne de `/Users/diego/Post-prod clients/SAVOIR-PUBLIE.md` (commit de la dernière publication), puis `git log --stat <ce commit>..HEAD -- .claude/skills .claude/agents GOUTS.md CARNET-DE-GOUT.md carnet` : c'est la liste de ce qui a changé.
3. Copie, sans option de suppression :
   `rsync -a --exclude .DS_Store ".claude/skills/" "/Users/diego/Post-prod clients/.claude/skills/"`
   `rsync -a --exclude .DS_Store ".claude/agents/directeur-artistique.md" "/Users/diego/Post-prod clients/.claude/agents/"`
   `rsync -a --exclude .DS_Store GOUTS.md CARNET-DE-GOUT.md "/Users/diego/Post-prod clients/.claude/savoir-robot/"` et `rsync -a --exclude .DS_Store carnet/ "/Users/diego/Post-prod clients/.claude/savoir-robot/carnet/"`
   Ne touche à aucun autre fichier du cabinet. Le skill `resolve-adaptation-format` est propre au cabinet : ne le supprime pas.
4. Si un skill a été renommé ou archivé chez moi, son ancienne copie reste dans le cabinet : dis-le à Diego et propose de la supprimer.
5. Ajoute une ligne à `SAVOIR-PUBLIE.md` : date, commit court, ce qui a changé en une phrase simple.
6. Confirme à Diego en une ligne.
