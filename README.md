# KDO
*KDO* est un jeu vidéo créé par un collègien français dans le but d'en faire le cadeau à une amie.

## Compilation
Vous utilisez [Linux ou MacOS](https://whatsmyos.com/) ? Pas de problèmes, il vous suffit de remplacer le préfixe *py* par *python* dans chaque commande.

Avant de compiler ce programme assurez vous que l'interpréteur de Python est installé sur votre machine en tapant `py --version` dans un invite de commande.
Si cela vous affiche une erreur, veuillez installer l'interpréteur de Python [ici](https://www.python.org/downloads/).

Dirigez vous ensuite dans le dossier *KDO* en utilisant les commande [*cd*](https://doc.ubuntu-fr.org/tutoriel/console_ligne_de_commande#:~:text=La%20commande%20cd%20vous%20permet,personnel%20(%2Fhome%2Futilisateur).&text=Contrairement%20%C3%A0%20la%20version%20Windows,utilisateur%20(ou%20du%20root).) puis tapez `py -m pip install -r requirements.txt` et `py -m PyInstaller --onefile --console main.py`. Vous trouverez ensuite votre exécutable dans le dossier *dist*.

## Remerciements
Merci à tout ceux qui m'ont aidé à maintenir ce projet.