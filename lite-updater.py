'''    _             _
  ___ | | _   _   __| | _ __   ___
 / _ \| || | | | / _` || '__| / _ |
|  __/| || |_| || (_| || |   |  __/
 \___||_| \__, | \__,_||_|    \___|
          |___/
___________________________________

 - codé en : UTF-8
 - langage : python3
 - GitHub  : github.com/elydre
 - Licence : GNU GPL v3
'''

import sys, os
from urllib.request import urlopen
from urllib.error import HTTPError


# to edit

# url de la raod de mise à jour
updfile = None
#chemin relatif a partire de la racine du script, "/" par defaut
chem = "/"
# langage de l'interface, "fr" ou "en"
lang = "fr"

# relative path

global PATH
PATH = os.path.dirname(sys.argv[0])

# languages

fr = {
"mkdir done":"dossier {} créé avec succès",
"mkdir err":"le dossier {} est déjà existant",
"wget done": "{} téléchargemé avec succès",
"cmd err": "commande inconnue ici -> {}",
"url err" : "url invalide ici -> {}",

"address err" : "adresse invalide"}

en = {
"mkdir done":"folder {} successfully created",
"mkdir err":"the folder {} is already existing",
"wget done": "{} successfully downloaded",
"cmd err": "unknown command here -> {}",
"url err" : "invalid url here -> {}",
"arg err": "unknown argument here -> {}",
"name err":"register {} not found in the road"}

lang = fr if lang == "fr" else en

# system function

def mkdir(chem, name):
    try:
        os.makedirs(PATH+chem+name)
        print(lang["mkdir done"].format(name))
    except FileExistsError: print(lang["mkdir err"].format(name))

def wget(chem, name, url):
    try:
        open(PATH + chem + name, 'wb').write(urlopen(url).read())
        print(lang["wget done"].format(name))
    except HTTPError: print(lang["url err"].format(url))

def mkchem(chem):
    dos = chem.split("/")
    while "" in dos: dos.remove("")
    for x in range(len(dos)):
        mkdir("","".join(f"/{dos[y]}" for y in range(x+1)))

# update launcher

def update(chem, updfile):
    mkchem(chem)
    try:
        l = urlopen(updfile).read().decode("utf-8").split("\n")
        for e in l:
            comp = str(e).split(" ")
            commande = comp[0].strip()
            arg = "".join(comp[1:]).split(",")
            if commande == "mkd":
                mkdir(chem, arg[0])
            elif commande == "wgt":
                wget(chem, arg[0],arg[1])
            elif commande != "":
                print(lang["cmd err"].format(commande))
    except HTTPError: print(lang["url err"].format(updfile))

if updfile != None and __name__ == "__main__":
    update(chem, updfile)