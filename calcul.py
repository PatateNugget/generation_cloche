import pyaudacity as pa
import pandas as pd
import numpy as np

def son_frequence(frequence,amplitude,duree):
    """ Génère une piste mono avec une fréquence, une amplitude et une durée donnée.
    Le son produit est un signal sinusoïdale avec une amplitude qui baisse de façon exponentiel."""
    
    # On génère une nouvelle piste en sélectionnant la durée nécessaire pour inclure un son sinusoïdale constant en fréquence et amplitude

    pa.do('NewMonoTrack')
    pa.do(f'SelectTime: Start="0" End="{duree}"')
    pa.do(f'Chirp: StartFreq="{frequence}" EndFreq="{frequence}" StartAmp="{amplitude}" EndAmp="{amplitude}"')

    # Puis son applique le fading exponentiel inverse

    fading_nl(duree,0.001,20)

def son_partiel(partiel,freq_fond,amplitude,duree):
    """ Génère une piste mono avec des partiels, une fréquence fondamentale, une amplitude et une durée donnée.
    Le son produit est un signal sinusoïdale avec une amplitude qui baisse de façon exponentiel."""
    
    # On génère une nouvelle piste en sélectionnant la durée nécessaire pour inclure un son sinusoïdale constant en fréquence et amplitude

    pa.do('NewMonoTrack')
    pa.do(f'SelectTime: Start="0" End="{duree}"')
    pa.do(f'Chirp: StartFreq="{freq_fond*partiel}" EndFreq="{freq_fond*partiel}" StartAmp="{amplitude}" EndAmp="{amplitude}"')

    # Puis son applique le fading exponentiel inverse

    fading_nl(duree=duree,seuil=0.001,iterations=20)

def fading_nl(duree,seuil,iterations):
    """Effectue une fermeture de son non linéaire, basé sur un modèle exponentiel"""

    # On calcule les paramètres d'un modèle exponentiel inverse qui représentera la baisse de l'amplitude au cours du temps.
    # Pour cela, on prend un paramètre alpha de sorte que la baisse de l'amplitude soit inférieur à un niveau donnée avec un nombre d'itération donnée.

    alpha=np.log(seuil)/duree

    temps=np.linspace(0,duree,iterations)

    amp_fade = np.exp(alpha*temps)

    fading = pd.DataFrame({"temps": temps,"amp_fade": amp_fade})

    # On modifie l'enveloppe avec les tableau de paramètres dont on dispose

    for index, ligne in fading.iterrows():
        pa.do(f'SetEnvelope: Time="{ligne["temps"]}" Value="{ligne["amp_fade"]}"')

def adsr(attack=0,decline=1,sustain=2,release=3):
    """ Travaille l'enveloppe de sorte qu'elle colle au modèle ADSR.
    Les paramètres sont des temps en secondes """
    
    # Pour le moment on donne des valeurs arbitraires aux amplitudes des différentes parties 
    # Le travail de l'enveloppe est ici linéaire

    pa.do(f'SetEnvelope: Time="0" Value="0.5"')
    pa.do(f'SetEnvelope: Time="{attack}" Value="1"')
    pa.do(f'SetEnvelope: Time="{attack+decline}" Value="0.7"')
    pa.do(f'SetEnvelope: Time="{attack+decline+sustain}" Value="0.7"')
    pa.do(f'SetEnvelope: Time="{attack+decline+sustain+release}" Value="0"')

