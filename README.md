Deux joueurs s'oppose sur une grille de 10 par 10  de A à J et de 1 a 10
chacun a une flotte composée de quelques bateaux d'une à cinq cases de long.

L'une des grilles représente la zone contenant sa propre flotte. Au début du jeu, chaque joueur place ses bateaux sur sa grille, en s'assurant que deux bateaux ne sont pas adjacents.

Chaque joueur  à son tour  ecrira ses coordonnées  (ex <<a1>>) le programme lui dira si le tir tombe à l'eau ou au contraire s'il touche un bateau. Dans ce dernier cas, il annonce <<touché>>

tout cela sera affiché sur une autre grille si il a touché ou pas avec une croix <<X>> sinon <<x>>, il n'est pas possible de jouer deux fois sur la meme case

celui qui detruit toute la flotte ennemie à gagné

bateaux:

Porte-avions de 5 de longueur
Croiseur de 4 de longueur
Contre-torpilleurs de 3 de longueur
Sous-marin de 3 de longueur
Torpilleur de 2 de longueur


installation:

    cloner le depot github: git clone https://github.com/Joss-inf/BatailleNavale.git
    installer : faite un git clone du projet

acces:

    acceder au repertoire: cd BatailleNavale/src

lancement:

    python3 main.py

Structure du projet:

    src: Contient le code source principal du jeu.
    data: Contient les fichiers de config/sauvegarde en format json.

Technologies utilisées

    Python: Langage de programmation principal.
    [Bibliothèques utilisées]: os,json,copy,

Auteur:
Josselin Bessière