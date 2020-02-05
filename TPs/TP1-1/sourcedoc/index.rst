---------------
Experimentateur
---------------


.. toctree::
   :maxdepth: 1

   experience.rst
   marker.rst
   
~~~~~~~~~~
Etat du TP
~~~~~~~~~~

Décrivez ici l'état d'avancement du TP.

~~~~~~~~~~~~~~~~~~~~~~
Réponses aux questions
~~~~~~~~~~~~~~~~~~~~~~

Indiquez ici les réponses aux questions posées dans le TP. Vous
reprendrez le numéro de la section et le numéro de la question. Par
exemple pour répondre à la question 3 de la section 2.4 vous
indiquerez.

   
Question 1.2.2
--------------

Pour étudier la complexité de cet algorithme on propose de compter le nombre de comparaisons effectuer entre les marqueurs (array markers et array positive markers).


Question 1.2.3
--------------

Non il n'existe pas un pire et un meilleur des cas, quelque soit l'ordre de  la liste on va effectuer le meme nombre de comparaison.


Question 1.2.4
--------------

C1(m,p) = la somme de i = 0 à i = p de (m-i) = m + (m-1) + (m-2) + ... + (m-p)


Question 1.3.1
--------------

On crée une boucle pour la liste des marqueurs et on cherche chaque element des marqueurs dans la liste des marqueurs positive en utilisant la recherche dichotomique
On a créer une varibale global dans le fichier sorting pour pouvoir trouver le nombre de comparaison qu'effectue la fonction merge_sort.
Et on affiche le nombre des comparaisons effectuer par la recherche dichotomique (Cd) et le nombre des comparaisons effectuer par la fonction merge_sort (Cm) et le nombre totale des des comparaisons effectuer: Cm + Cd 


Question 1.3.2
--------------

Oui, il existe un pire des cas pour cet algorithme si les marqueurs positives sont les marqueurs les plus petit de la liste.


Question 1.4.2
--------------

Oui, car on utilise le mergesort et ce dernier a un pire et un meilleur des cas, mais si on compte pas les nombre de comparaisons effecter par mergesort on a pas de pire et meilleur cas, car pour chaque marqueur on fait une seule comparaison. C3(m) = la longeur de m array des marqueurs et donc le nombre totale des comparaisons et Cm1 = le nombre de comparaison mergesort des markers et Cm2 = le nombre de comparaison mergesort des markers positive + C3(m).


 
