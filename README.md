# Kalkulator-z-odwrotn-notacj-polsk-
Langage utilisée : Python3 et polonais

Programme à utiliser sur VSCode pour un fonctionnement optimal (afin de bien voir le fonctionnement de la dernière ligne du code (le commentaire))

Ceci est un programme représentant une calculatrice en notation polonaise inversée (uniquement l'opération "+").
Le calcul en polonaise inversée s'éxécute comme ceci :
Nous rentrons ceci :
10 2 + = 

La calculatrice rangera dans une pile 10 et 2, ira chercher l'opérateur suivant, effectura l'opération 10 + 2 et retournera 12, le résultat.
Il est possible d'effectuer plusieurs opérations comme ceci :
10 2 + 10 3 + + 10 4 + + =
La présence du "=" à la fin est necessaire.

Toutefois, afin de rendre l'éxécution du code compliqué pour pas grand chose, nous avons fait le choix de calculer bit à bit nos opérandes et de stocker nos nombres dans une pile un peu spéciale.

En effet, la pile n'est pas une liste, un tableau ou un dictionnaire. On a choisit plus compliqué, moins intuitif pour rendre le programme ridiculement stupide.
Ainsi, lors de l'éxécution de notre programme, nous ouvrons ce dernier pour y enregistrer directement à la dernière ligne nos nombres et les résultats intermédiaire du calcul en binaire sous forme d'un commentaire dans la derniere ligne de notre programme.
Nous supprimons cette ligne pour la remplir à nouveau avec de nouvelles valeures quand cela est necessaire. Nous allons donc chercher à la dernière ligne de notre programme les informations qui nous intéresse pour effectuer nos calculs intermédiaires.

Bien evidemment, les boucles, les conditions et les variables sont toutes mal formulées.
