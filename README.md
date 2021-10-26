# Démarrage rapide
Online-update est un programme python permettant de mettre a jour des dossier et de fichier depuis une adresse web.
# Mode préconfiguré
Le fichier `update.py` permet au créateur d’un programme de pré-configuré online-update pour directement téléchargé depuis une adresse web.\
Pour cela il suffit de modifier `updfile = None` à la ligne 22 par l’adresse du fichier d’update.\
Il est aussi possible de modifier a langue de l’updater, français (fr) ou anglais (en) a la ligne 23.
# Mode cli
Le second fichier, `cli-update.py` affiche une interface cli permettant de saisir l’adresse des commandes.\
## Commandes

### LANG
`lang` permet de saisir la langue de l'updater, en/fr

```
lang <langue>
lang fr
```
### DL
`dl` permet de téléchargé un registre directement depuis son adresse

```
dl <chemin> <adresse>
dl /main https://raw.githubusercontent.com/pf4-DEV/glade/main/update.txt
```

### ROAD
`road` permet de géré la liste des fichier de redirection:\
`road list` affiche la liste\
`road add` ajoute une adresse a la liste\
`road del` supprime une adresse a la liste\
`road read` lie les fichier de redirection

### RDL
`rdl` téléchargé un registre depuis les fichier de redirection:\
```
dl <chemin> + <nom>
dl /main glade
```

# Créé un registre d’update
Le registre d’update différencie tout les dossier et fichier a créer et/ou télécharger.
## Création du dossier
*l’entièreté des chemin de fichier son en relatif par rapport a l’updater\
La commande `mkd` suivit du nom du dossier a créé permet de créer un dossier:
```
mkd /mod
```
## Téléchargement de fichier
La commande `wgt` suivit du nom du ficher et de son adresse (séparé par une virgule) permet de téléchargé un fichier:
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

# Créé un fichier de routage

le ficher de routage doit contenir le nom et d'adresse de redirection séparé par une virgule
```
glade, https://raw.githubusercontent.com/pf4-DEV/glade/main/update.txt
```