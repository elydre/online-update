# online-update
## démarrage rapide
online-update est un programme python permettant de mettre a jour des dossier et de fichier depuis une adresse web.
## Mode pré-configuré
Deux mode sont prévue, le premier permet au créateur d’un programme de pré-configuré online-update pour directement téléchargé depuis une adresse web.\
Pour cela il suffit de modifier `updfile = None` à la ligne 22 par l’adresse du fichier d’update.\
Il est aussi possible de modifier a langue de l’updater, français (fr) ou anglais (en) a la ligne 23.
## Mode cli
Dans la cas ou la ligne 22 et laissé à None, l’updater affiche une interface cli permettant de saisir l’adresse du  registre
## Créé un registre d’update
le registre d’update référenci tout les dossier et fichier a créer et/ou télécharger.
### Création du dossier
*l’entièreté des chemin de fichier son en relatif par rapport a l’updater*\
la commande `mkd` suivit du nom du dossier a créé permet de créer un dossier:
```py
mkd /mod
```
### Téléchargement de fichier
la commande `wgt` suivit du nom du ficher et de son adresse (séparé par une virgule) permet de téléchargé un fichier:
```
wgt /direct-time.pyw, https://raw.githubusercontent.com/pf4-DEV/glade/main/direct-time.pyw
```