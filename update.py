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

fr = {"mkdir done":"dossier {} créé avec succès",
      "mkdir err":"le dossier {} est déjà existant",
      "wget done": "{} téléchargemé avec succès",
      "cmd err": "commande inconnue ici -> {}"}

en = {"mkdir done":"folder {} successfully created",
      "mkdir err":"the folder {} is already existing",
      "wget done": "{} successfully downloaded",
      "cmd err": "unknown command here -> {}"}

updfile = "https://raw.githubusercontent.com/pf4-DEV/online-update/main/test.txt"
lang = fr

def mkdir(name):
    try:
        os.makedirs(PATH+name)
        print(lang["mkdir done"].format(name))
    except FileExistsError: print(lang["mkdir err"].format(name))

def wget(name,address):
    open(PATH + name, 'wb').write(urlopen(address).read())
    print(lang["wget done"].format(name))

def update(updfile):
    l = urlopen(updfile).read().decode("utf-8").split("\n")
    for e in l:
        comp = str(e).split(" ")
        commande = comp[0].strip()
        arg = "".join(comp[1:len(comp)]).split(",")
        if commande == "mkd":
            mkdir(arg[0])
        elif commande == "wgt":
            wget(arg[0],arg[1])
        elif commande != "":
            print(lang["cmd err"].format(commande))

update(updfile)