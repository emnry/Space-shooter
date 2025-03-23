# 👾 Space Shooter - Python Space Shooter 

Ce projet est un jeu d'arcade développé en Python avec la bibliothèque Pygame, inspiré des classiques tels que Space Invaders. Le joueur doit défendre sa station spatiale contre des vagues d'ennemis variés, allant des astéroïdes aux créatures mythologiques. Le jeu propose une expérience immersive avec des cinématiques, un système de score et des modes de triche pour explorer le gameplay. Le tout est enrichi par des effets sonores dynamiques et une gestion des collisions et des vies du joueur.

## ✨ Fonctionnalités

* Vagues d'ennemis variés (astéroïdes ☄️, ennemis élémentaires : plantes, feu, roches, eau, et fantastiques : trolls, boss démoniaque ).
* Cinématiques entre les vagues pour une expérience plus immersive.
* Système de score et de meilleur score.
* Mode de triche (lasers illimités, invincibilité) pour tester le jeu.
* Effets sonores pour les collisions, les tirs et les éliminations.
* Gestion des collisions et des vies du joueur.
* ⏩ Possibilité de passer les cinématiques.

## ️ Installation

1.  Assurez-vous d'avoir Python 3 et Pygame installés.
2.  Clonez ce dépôt Git :
   
    `git clone https://github.com/votre-utilisateur/votre-repo.git`

4.  Naviguez jusqu'au répertoire du projet :

    `cd votre-repo`

5.  Exécutez le jeu :

    `python main.py`

##  Dépendances

* Pygame

##  Structure du projet

* `startup.py` : Fichier principal du jeu.
* `players.py` : Gestion du joueur.
* `opponents.py` : Gestion des ennemis.
* `cutscenes.py` : Gestion des cinématiques.
* `laser.py` : Gestion des lasers du joueur.
* `textures/` : Dossier contenant les images du jeu .
* `sounds/` : Dossier contenant les effets sonores.
* `meilleur_score.txt`: Fichier contenant le meilleur score.
* `speechs.txt`: Fichier contenant les dialogues de cinématiques.

## ⚙️ Paramètres changeables

* `toggle_hitbox` : Afficher les contours des zones de collision .
* `toggle_cutscenes` : Activer les cinématiques .
* `randomwave` : Vagues d'attaques aléatoires .
* `toggle_next_wave` : Décider de la prochaine vague ⏭️.
* `next_wave` : Liste des vagues suivantes .
* `toggle_godmode` : Mode dieu (invincibilité) ️.
* `toggle_cheat` : Mode lasers illimités .

## ️🎮 Commandes

* Flèches directionnelles : Déplacement du joueur ➡️⬅️⬆️⬇️.
* Barre d'espace : Tirer.
* Échap : Quitter le jeu.
* Maj : Utiliser le boost ➜ Déplacement rapide et tir augmenté.
* 1 : Passer les cinématiques ⏩.
