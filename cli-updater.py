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

# relative path

global PATH
PATH = os.path.dirname(sys.argv[0])

# list of road

road = ["https://raw.githubusercontent.com/pf4-DEV/online-update/main/road/main.txt"]

# languages

fr = {"mkdir done":"dossier {} créé avec succès",
      "mkdir err":"le dossier {} est déjà existant",
      "wget done": "{} téléchargemé avec succès",
      "cmd err": "commande inconnue ici -> {}",
      "address err" : "adresse invalide",
      "arg err": "argument inconnu ici -> {}"}

en = {"mkdir done":"folder {} successfully created",
      "mkdir err":"the folder {} is already existing",
      "wget done": "{} successfully downloaded",
      "cmd err": "unknown command here -> {}",
      "address err" : "invalid address",
      "arg err": "unknown argument here -> {}"}

lang = en

# system function

def mkdir(chem, name):
    try:
        os.makedirs(PATH+chem+name)
        print(lang["mkdir done"].format(name))
    except FileExistsError: print(lang["mkdir err"].format(name))

def wget(chem, name, address):
    open(PATH + chem + name, 'wb').write(urlopen(address).read())
    print(lang["wget done"].format(name))

def mkchem(chem):
    dos = chem.split("/")
    while "" in dos: dos.remove("")
    for x in range(len(dos)):
        mkdir("","".join(f"/{dos[y]}" for y in range(x+1)))

# update launcher

def update(chem, updfile):
    mkchem(chem)
    l = urlopen(updfile).read().decode("utf-8").split("\n")
    for e in l:
        comp = str(e).split(" ")
        commande = comp[0].strip()
        arg = "".join(comp[1:len(comp)]).split(",")
        if commande == "mkd":
            mkdir(chem, arg[0])
        elif commande == "wgt":
            wget(chem, arg[0],arg[1])
        elif commande != "":
            print(lang["cmd err"].format(commande))

# cli

while True:
    ipt = input("~} ").split(" ")
    for _ in range(10 - len(ipt)): ipt.append("")
    commande = ipt[0]
    if commande == "lang":
        if ipt[1] == "en": lang = en
        elif ipt[1] == "fr": lang = fr
        else: print(lang["arg err"].format(ipt[1]))
    elif commande == "dl":
        try: update(ipt[1],ipt[2])
        except: print(lang["address err"])
    elif commande in ["road", "r"]:
        if ipt[1] == "list":
            print(road)
        elif ipt[1] == "add":
            road.append(ipt[2])
        elif ipt[1] == "del":
            try: road.remove(ipt[2])
            except: print(lang["address err"])
        else: print(lang["arg err"].format(ipt[1]))