# RaynalBird

**Contexte**

Notre application est un jeu vidéo développé avec Python 3.6 et utilisant la bibliothèque Pygame. Le but du jeu consiste à éviter pour le joueur, les différents tuyaux se présentant devant lui. Si le joueur échoue et touche l’un des obstacles, il doit alors recommencer la partie du début et avec pour objectif d’aller le plus loin possible. Il existe 3 niveaux de difficultés :
- Le niveau « Easy » : Le personnage avance lentement, laissant le temps d’éviter facilement les obstacles.
- Le niveau « Medium » : Le personne avance de manière assez rapide.
- Le niveau « Hard Core » : Le personne avance de manière extrêmement rapide. 

Afin de pouvoir suivre la progression du joueur, le score est présent en haut à gauche de l’écran lors des parties. 



# Guide d’utilisation
Avant de pouvoir utiliser notre jeu vidéo, il est nécessaire d’avoir au préalable installé : 
	
	•	Python 3.6
	•	Pygame
	
Le lancement de l’application s’effectue par l’ouverture du fichier « main.py » avec l’IDE de Python, une fois dessus, il suffit de démarrer le code avec la touche F5. La fenêtre avec le menu du jeu est alors visible.

Une fois dessus, il suffit alors d’appuyer sur une touche quelconque comme « Espace » et de choisir le niveau de difficulté désiré avec les touches F1 pour le niveau facile, F2 pour le niveau moyen et F3 pour le niveau difficile.

Le joueur se retrouve alors immédiatement dans une nouvelle partie et doit appuyer sur la touche « Espace » afin d’éviter les obstacles présent devant lui.

En cas d’échec de la part du joueur, un écran de fin du jeu apparaît, avec la possibilité pour lui de relancer une nouvelle partie.

## Répartition des tâches
Le développement de l’application a été réparti de la manière suivante : 

	o	Jean DEYEHE : Développement du moteur principal du jeu, avec les niveaux de difficultés, le calcul du score et l’intégration des bandes sonores.
	o	Benoît PINAULT : Développement du socle de base du projet avec l’intégration de Pygame et réalisation des interfaces avec images.
	o	Mickael MOREIRA : Développement et amélioration de certaine partie du moteur du jeu et réalisation de la documentation.