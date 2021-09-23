Présentation du travail : Problème des pichets

Description du problème :

	- 1 pichet de contenance maximum 5 (noté cm1), avec une contenance actuelle de 5 (notée ca1)
	- 1 pichet de contenance maximum 2 (noté cm2), avec une contenance actuelle de 0 (notée ca2)

	Objectif : Que le pichet 2 est une contenance de 1.

Dans le projet j'ai décidé de représenter un état de cette manière : (cm1, ca1, cm2, ca2) avec :
	- cm1 -> contenance maximale du pichet 1
	- ca1 -> contenance actuelle du pichet 1
	- cm2 -> contenance maximale du pichet 2
	- ca2 -> contenance actuelle du pichet 2

Pour arriver au résultat, j'ai défini 3 actions possibles sur le pichet (les 3 actions précisées dans le sujet) :

	- jeterCompletement(etat) : Cette fonction prend un etat en paramètre 
et vide complètement le contenu du pichet.
	- viderCompletementPichetAutre(etat) : Cette fonction prend un etat en 
paramètre et vide complètement le contenu d'un pichet dans l'autre pichet, si ce dernier ne déborde
pas.
	- viderPartiellementPichetAutre(etat) : Cette fonction prend un etat en
paramètre et vide partiellement le contenu d'un pichet dans l'autre, avec les contraintes
que le pichet receveur doit être remplit, et que le pichet emetteur ait une plus grande contenance actuelle que
le pichet receveur (sinon le pichet receveur ne pourra pas être remplit".

J'ai ensuite défini des getteurs getChemin(noeud), getEtat(noeud), une fonction d'affichage afficher_sol(noeud) et
une fonction dejavu(etat,chemin) qui nous indique si un état est déjà présent dans les noeuds, auquel cas on ne 
le remet pas. 

J'ai enfin défini, à la manière de l'exercice 1 du td1, les fonctions noeudFils(noeud) et rp_rec(noeud) qui,
à l'aide de la définition des états et des actions, vont chercher le résultat. 

On arrive alors à un résultat : 
Solution :
(5, 5, 2, 0)
(5, 3, 2, 2)
(5, 3, 2, 0)
(5, 1, 2, 2)
(5, 1, 2, 0)
(5, 0, 2, 1)
Longueur : 6

Cela veut dire que, partant de l'état initial, on doit réaliser 5 actions pour arriver à l'état final. Cela nous 
fait 6 états différents (donc une solution de longueur 6).