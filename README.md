# online-update
## Démarrage rapide
Online-update est un programme python permettant de mettre a jour des dossier et de fichier depuis une adresse web.
## Mode préconfiguré
Deux mode sont prévue, le premier permet au créateur d’un programme de pré-configuré online-update pour directement téléchargé depuis une adresse web.\
Pour cela il suffit de modifier `updfile = None` à la ligne 22 par l’adresse du fichier d’update.\
Il est aussi possible de modifier a langue de l’updater, français (fr) ou anglais (en) a la ligne 23.
## Mode cli
Dans la cas ou la ligne 22 et laissé à None, l’updater affiche une interface cli permettant de saisir l’adresse du  registre
## Créé un registre d’update
Le registre d’update référencie tout les dossier et fichier a créer et/ou télécharger.
### Création du dossier
*l’entièreté des chemin de fichier son en relatif par rapport a l’updater*\
La commande `mkd` suivit du nom du dossier a créé permet de créer un dossier:
```
mkd /mod
```
### Téléchargement de fichier
La commande `wgt` suivit du nom du ficher et de son adresse (séparé par une virgule) permet de téléchargé un fichier:
```
wgt /direct-time.pyw, https://raw.githubusercontent.com/pf4-DEV/glade/main/direct-time.pyw
```
## Exemples

registre de mise a jour de Glade\
https://raw.githubusercontent.com/pf4-DEV/glade/main/update.txt
```
mkd /container
mkd /system
mkd /system/glade
mkd /system/mod

wgt /glade-cli.py, https://raw.githubusercontent.com/pf4-DEV/glade/main/glade-cli.py
wgt /system/glade/Compiler.py, https://raw.githubusercontent.com/pf4-DEV/glade/main/system/glade/Compiler.py
wgt /system/glade/Tools.py, https://raw.githubusercontent.com/pf4-DEV/glade/main/system/glade/Tools.py
wgt /system/mod/Cytron.py, https://raw.githubusercontent.com/pf4-DEV/cytron/main/cytron.py
wgt /system/mod/ColorPrint.py, https://raw.githubusercontent.com/pf4-DEV/Color-Printer/main/ColorPrint.py
wgt /system/settings.txt, https://raw.githubusercontent.com/pf4-DEV/glade/main/system/settings.txt
wgt /container/t.py, https://raw.githubusercontent.com/pf4-DEV/glade/main/container/t.py
wgt /direct-time.pyw, https://raw.githubusercontent.com/pf4-DEV/glade/main/direct-time.pyw
wgt /system/glade/TEyes.py, https://raw.githubusercontent.com/pf4-DEV/glade/main/system/glade/TEyes.py
```