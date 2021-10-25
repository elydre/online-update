'''
--|~|--|~|--|~|--|~|--|~|--|~|--

██  ████        ██████        ██
████    ██     ██           ████
██      ██   ████████     ██  ██
████████       ██       ██    ██
██             ██       █████████
██             ██             ██
██
 - codé en : UTF-8
 - langage : python 3
 - GitHub  : github.com/pf4-DEV
--|~|--|~|--|~|--|~|--|~|--|~|--
'''

import sys, os
from urllib.request import urlopen

global PATH
PATH = os.path.dirname(sys.argv[0])

fr = {"mkdir done":"dossier {} créé avec succès"}
en = {"mkdir done":"folder {} successfully created"}

updfile = "https://raw.githubusercontent.com/pf4-DEV/online-update/main/test.txt"
lang = fr

def mkdir(name):
    try:
        os.makedirs(PATH+name)
        print(lang["mkdir done"].format(name))
    except FileExistsError: print(f"le dossier {name} est déjà existant")

def wget(name,address):
    open(PATH + name, 'wb').write(urlopen(address).read())
    print(f"{name} téléchargemé avec succès")

def update(updfile):
    l = urlopen(updfile).read().decode("utf-8").split("\n")
    for e in l:
        comp = str(e).split(" ")
        commande = comp[0].strip()
        arg = "".join(comp[1:len(comp)]).split(",")
        print(commande,arg)
        if commande == "mkd":
            mkdir(arg[0])
        elif commande == "wgt":
            wget(arg[0],arg[1])
        elif commande != "":
            print(f"commande inconnue ici -> {commande}")

update(updfile)