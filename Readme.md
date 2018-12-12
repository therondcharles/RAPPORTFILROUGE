# Architecture projet

## Branches:
Tout d'abord la gestion des branches:
Chaque membre possede sa branche personnelle pour faire ses développements.
Puis une fois les nouvelles fonctionnalités testées elles seront merged dans la branche master.

Les branches sont donc:

| Branche | Prénom |
|---------|:--------:|
| master |  prod |
| kpe | Karine |
| ica | Ioan |
| smu | Stéphane |
| cth | Charles |


## Arborescence:
Dans cette section reside l'architecture des dossiers.
 * Exploration
 * Paircoding
 * Production
   * git_merge.py ( gestion des merges dans le cas des unions )
 * fonctionCommune.py ( fonction utile à chacun )

## Gestion de code

Afin de ne pas douter du fonctionnement de git, voila quelques ressources utiles pour mieux comprendre son fonctionnement.

[Introduction à git en 30 min](https://www.youtube.com/watch?v=hPfgekYUKgk)

[Collaboration sur git hub](https://github.com/codepath/android_guides/wiki/Collaborating-on-Projects-with-Git)

[Compréhension du merge union](https://stackoverflow.com/questions/46182123/how-to-resolve-a-git-conflict-by-keeping-all-additions-from-both-sides)

Les cas problématique sont les cas d'union qui sont gerés par la fonction ```git_merge_union()```. La fonction retourne les lignes de commandes à executer pour
selon le sens de merge
### master vers branche utilisateur

git_merge_union("master","cth",["fonctionCommune.py"])
 > git checkout cth

 > git merge master

 > git show :1:fonctionCommune.py > fonctionCommune.py.base

 > git show :2:fonctionCommune.py > fonctionCommune.py.ours

 > git show :3:fonctionCommune.py > fonctionCommune.py.master

 > mv fonctionCommune.py.master fonctionCommune.py

 > git merge-file --union fonctionCommune.py fonctionCommune.py.base fonctionCommune.py.ours

 > rm fonctionCommune.py.base fonctionCommune.py.ours

 > git add fonctionCommune.py

 > git commit -m " merge master "

 > git push origin  cth

### branche vers master

git_merge_union("cth","master",["fonctionCommune.py"])
 > ```git checkout master
 git merge cth
 git show :1:fonctionCommune.py > fonctionCommune.py.base
 git show :2:fonctionCommune.py > fonctionCommune.py.ours
 git show :3:fonctionCommune.py > fonctionCommune.py.cth
 mv fonctionCommune.py.cth fonctionCommune.py
 git merge-file --union fonctionCommune.py fonctionCommune.py.base fonctionCommune.py.ours
 rm fonctionCommune.py.base fonctionCommune.py.ours
 git add fonctionCommune.py
 git commit -m " merge cth "
 git push origin  master```