# Gégnération d'un son cloche avec Audacity

Cet outil permet de générer un son de cloche pour des paramètres donnés depuis un fichier csv avec le logiciel Audacity. Il a été fait dans le cadre d'un projet de recherche en Licence 1. 

# Utilisation 

## Au préalable

Pour utiliser ce code, il faut au préalable télécharger le logiciel Audacity dans sa dernière version. Pour pouvoir utiliser les macros dans Audacity, il faut ensuite se rendre dans :

Edit > Preferences 

Une fenêtre s'ouvre, dans **Modules**, il faut activer _mod_script_pipe_ . A noter que sur Windows, il se peut que la socket ne fonctionne pas correctement notamment pour le travail de l'enveloppe, ce qui est moins le problème sous une distribution Linux.

Il faut aussi disposer de python dans une version supérieure à la 3.9. Les bibliothèques Python suivantes sont nécessaires :  

* pandas
* numpy
* argparse
* pyaudacity

Il est possible de les retrouver au moyen de **pip**.

## Utilisation 

Pour utiliser le script, il faut se mettre dans un terminal et utiliser de la sorte :

``` python generer_son.py --infile -i [fichier] [--partiel -p] [--fondamentale -f frequence] --attaque -a [temps] --maintien -m [temps] --declin -d [temps] --relache -r [temps] ```

Il est nécessaire d'utiliser un fichier csv dont le séparateur est ";", qui dispose de trois colonnes avec les paramètres suivants : frequence ou partiel (selon que l'on veut générer directement les fréquences ou les partiels à partir d'une fréquence fondamentale), amplitude, duree. On précise dans le paramètre -i le répertoire du fichier. Si l'on souhaite préciser les partiel, il faut mettre l'option --p  avec nécessairement l'option -f et la fréquence fondamentale. Enfin, on précise les paramètres du modèle ASDR avec les paramètres restant. Le son est alors généré dans le logiciel Audacity. Des fichiers d'exemples sont fournis.
