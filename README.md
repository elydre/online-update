# Démarrage rapide
Online-update est un programme python permettant de mettre a jour des dossier et de fichier depuis une url web.
# Mode préconfiguré
Le fichier `update.py` permet au créateur d’un programme de pré-configuré online-update pour directement téléchargé depuis une url web.\
Pour cela il suffit de modifier `updfile = None` à la ligne 22 par l’url du fichier d’update.\
Il est aussi possible de modifier a langue de l’updater, français (fr) ou anglais (en) a la ligne 23.
# Mode cli
Le second fichier, `cli-update.py` affiche une interface cli permettant de saisir l’url des commandes.\
## Commandes

### LANG
`lang` permet de saisir la langue de l'updater, en/fr

```
lang <langue>
lang fr
```
### DL
`dl` permet de téléchargé un registre directement depuis son url

```
dl <chemin> <url>
dl /main https://raw.githubusercontent.com/pf4-DEV/glade/main/update.txt
```

### ROAD
`road` permet de géré la liste des fichier de redirection:\
`road list` affiche la liste\
`road add` ajoute une url a la liste\
`road del` supprime une url a la liste\
`road read` lie les fichier de redirection

### RDL
`rdl` téléchargé un registre depuis les fichier de redirection:\
```
dl <chemin> + <nom>
dl /main glade
```

# Créer un registre d’update
Le registre d’update différencie tout les dossier et fichier à créer et/ou télécharger.
## Création du dossier
l’entièreté des chemins de fichier son en relatif par rapport a l’updater\
La commande `mkd` suivit du nom du dossier a créé permet de créer un dossier:
```
mkd /mod
```
## Téléchargement de fichier
La commande `wgt` suivit du nom du ficher et de son url (séparé par une virgule) permet de téléchargé un fichier:
```
wgt /direct-time.pyw, https://raw.githubusercontent.com/pf4-DEV/glade/main/direct-time.pyw
```

## Exemple

registre de mise a jour de Glade\
https://raw.githubusercontent.com/pf4-DEV/glade/main/update.txt
```
mkd /container
...

wgt /glade-cli.py, https://raw.githubusercontent.com/pf4-DEV/glade/main/glade-cli.py
wgt /system/glade/Compiler.py, https://raw.githubusercontent.com/pf4-DEV/glade/main/system/glade/Compiler.py
...
```

# Créer un fichier de routage

le ficher de routage doit contenir le nom et d'url de redirection séparé par une virgule
```
glade, https://raw.githubusercontent.com/pf4-DEV/glade/main/update.txt
```