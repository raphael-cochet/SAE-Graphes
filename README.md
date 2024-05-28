<h3 style="text-align: center;">Raphaël COCHET - Arthur JOUAN</h5>
<h1 style="text-align: center;">Rendu SAE BD / Rapport</h1>

Q6.3
La fonction collaborateur_proche utilise l'algorithme de parcours en largeur (BFS) pour déterminer tous les acteurs qui se trouvent à une distance maximale k d'un acteur donné dans un graphe. Cet algorithme est un algorithme classique en théorie des graphes, souvent utilisé pour explorer les nœuds d'un graphe de manière systématique.

Pour déterminer si un acteur B se trouve à une distance exacte de k d’un acteur A, on peut utiliser la fonction collaborateur_proche en vérifiant si l'acteur B fait partie de l'ensemble des acteurs retournés par la fonction lorsqu'elle est appelée avec l'acteur A et la distance k. Cependant, cette approche ne donne pas directement la distance exacte, elle vérifie juste si l'acteur est à une distance inférieure ou égale à k.

Pour trouver la distance entre deux acteurs A et B, nous pouvons réutiliser l'idée du BFS mais avec une légère modification pour retourner la distance au lieu de l'ensemble des nœuds. En BFS standard, la distance de chaque nœud à la source est enregistrée.

Complexité de l'algorithme
La complexité du BFS est 
𝑂(𝑉+𝐸) où 𝑉 est le nombre de nœuds (acteurs) et 𝐸 est le nombre d'arêtes (collaborations) dans le graphe. Cette complexité s'applique aussi à la fonction collaborateur_proche.


Q6.4
c'est appelée l'excentricité