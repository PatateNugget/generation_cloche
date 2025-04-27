import calcul as cl
import argparse as ap
import pandas as pd
import pyaudacity as pa

#### Récupérations données

parser = ap.ArgumentParser()
parser.add_argument("-a","--attaque",type=float)
parser.add_argument("-d","--declin",type=float)
parser.add_argument("-m","--maintien",type=float)
parser.add_argument("-r","--relache",type=float)
parser.add_argument("-p","--partiel",action=ap.BooleanOptionalAction)
parser.add_argument("-f","--fondamentale",type=int)
parser.add_argument("-i","--infile",type=str)

arguments = parser.parse_args()

attaque=arguments.attaque
maintien=arguments.maintien
declin=arguments.declin
relache=arguments.relache
partiel=arguments.partiel
fondamentale=arguments.fondamentale
fichier=arguments.infile

parametres_sons=pd.read_csv(fichier,sep=";")

#### Génération son
if partiel:
    for index,ligne in parametres_sons.iterrows():
        cl.son_partiel(partiel=ligne["partiel"],
                       freq_fond=fondamentale,
                       amplitude=ligne["amplitude"],
                       duree=ligne["duree"])
else :
    for index,ligne in parametres_sons.iterrows():
        cl.son_frequence(frequence=ligne["frequence"],
                         amplitude=ligne["amplitude"],
                         duree=ligne["duree"])

#### Mix de toutes les piste pour n'en faire qu'une

pa.do('SelectAll:')
pa.do('MixAndRender')

#### Travail de l'enveloppe

cl.adsr(attack=attaque,
        decline=declin,
        sustain=maintien,
        release=relache)
