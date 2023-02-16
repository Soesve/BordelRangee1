"""
Jeu de permutation dans lequel il faut remettre dans l'ordre !
"""

from os import environ
from random import shuffle

# Fonction d'input d'un point en 2D séparés par une virgule (int)
def input_point_2D_int(phrase:str) -> list[int,int]:
    """
    Fonction d'input d'un point en 2D séparés par une virgule (int)
    """
    sommet_str = input(phrase)
    if not "," in sommet_str :
        return input_point_2D_int(phrase)
    else :
        index_virgule = sommet_str.find(",")
        abscisse_str = sommet_str[:index_virgule]
        ordonnee_str = sommet_str[index_virgule+1:]
    try :
        abscisse = int(abscisse_str)
        ordonnee = int(ordonnee_str)
    except :
        return input_point_2D_int(phrase)

    return [abscisse,ordonnee]

# Fonction d'affichage d'une liste en tableau
def AffichageTableau(liste:list=[[1,2,3],[4,5,6],[7,8,9]]) -> None:
    """ 
    Affiche une liste d'éléments sous forme de tableau
    /!\ Chaque élément doit ne comporter qu'un seul caractère pour un affichage optimal
    /!\ La liste doit comporter exactement 9 éléments
    Entrée : list de 3 éléments qui sont eux mêmes des listes de 3 éléments qui ne font qu'un seul caractère
    Exemple : [[1,2,3],[4,5,6],[7,8,9]]
    Sortie : None
    """
    print("\n")
    print("=============")
    print("|",liste[0][0],"|",liste[0][1],"|",liste[0][2],"|")
    print("=============")
    print("|",liste[1][0],"|",liste[1][1],"|",liste[1][2],"|")
    print("=============")
    print("|",liste[2][0],"|",liste[2][1],"|",liste[2][2],"|")
    print("=============")
    print("\n")
    return None

# Boucle de demande à l'utilisateur
def input_ge(phrase):
    """
    Boucle de demande à l'utilisateur
    On n'accepte que les coordonnées 1, 2 ou 3
    """
    point = input_point_2D_int(phrase)
    if (point[0] == 1 or point[0] == 2 or point[0] == 3) and (point[1] == 1 or point[1] == 2 or point[1] == 3) :
        return point
    else :
        return input_ge(phrase)

# On définit une liste de départ
liste = [1,2,3,4,5,6,7,8,9]
# On mélange les éléments de la liste
shuffle(liste)
# On change la liste en liste de 3 listes de 3 int
liste = [[liste[0],liste[1],liste[2]],[liste[3],liste[4],liste[5],],[liste[6],liste[7],liste[8]]]

# Affichage du début du jeu
print("\nLe but du jeu est d'arriver au tableau ordonné suivant : ")
AffichageTableau([[1,2,3],[4,5,6],[7,8,9]])
print("==========================\n\nVous pouvez échanger deux nombres en saisissant leurs coordonnées \
\n\n==========================\n\nC'est parti !\n\n==========================")

# Tant que la liste n'est pas ordonnée, on joue
while liste != [[1,2,3],[4,5,6],[7,8,9]] :
    # On affiche le tableau à l'utilisateur
    AffichageTableau(liste)
    # L'utilisateur saisit 2 coordonnées à échanger
    id_1 = input_ge("Entrer les coordonnées de la 1ère case à échanger (Séparées par une virgule) : ")
    id_2 = input_ge("Entrer les coordonnées de la 2ème case à échanger (Séparées par une virgule) : ")
    # On commence à 0 en python
    id_1[0] -= 1
    id_2[0] -= 1
    id_1[1] -= 1
    id_2[1] -= 1
    # On échange les positions dans la liste
    liste[id_2[0]][id_2[1]], liste[id_1[0]][id_1[1]] = liste[id_1[0]][id_1[1]], liste[id_2[0]][id_2[1]]

# Affichage de la victoire
AffichageTableau(liste)
print("==========================\n\nC'est gagné !\n\n==========================\n")