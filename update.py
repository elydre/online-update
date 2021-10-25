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

# to edit

updfile = None
lang = "fr"

# relative path

global PATH
PATH = os.path.dirname(sys.argv[0])

# languages

fr = {"mkdir done":"dossier {} créé avec succès",
      "mkdir err":"le dossier {} est déjà existant",
      "wget done": "{} téléchargemé avec succès",
      "cmd err": "commande inconnue ici -> {}",
      "address err" : "adresse invalide"}

en = {"mkdir done":"folder {} successfully created",
      "mkdir err":"the folder {} is already existing",
      "wget done": "{} successfully downloaded",
      "cmd err": "unknown command here -> {}",
      "address err" : "invalid address"}

lang = fr if lang == "fr" else en

# system function

def mkdir(name):
    try:
        os.makedirs(PATH+name)
        print(lang["mkdir done"].format(name))
    except FileExistsError: print(lang["mkdir err"].format(name))

def wget(name,address):
    open(PATH + name, 'wb').write(urlopen(address).read())
    print(lang["wget done"].format(name))

# update launcher

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

if updfile is None:
    while True:
        try: update(input("-> "))
        except: print(lang["address err"])
else:
    update(updfile)