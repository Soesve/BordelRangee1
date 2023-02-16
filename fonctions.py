"""
    Liste des fonctions pour les champs de formulaire
    Author : Jeremy
    Date : 16/02/2023
    Version : 0.1
"""

def inputInt(texte = "Veuillez entrer un nombre entier : ") -> int:
    """ On demande un nombre à l'utilisateur, et on vérifie que c'est bien un entier. Si non, on continue de demander un nombre à l'utilisateur.

    Args:
        texte (str, optional): texte à afficher pour demander un nombre à l'utilisateur. Par défaut, on affiche "Veuillez entrer un nombre entier : ".

    Returns:
        int: nombre entier
    """
    erreur = 1
    nombre = input(texte)
    while erreur:
        try:
            nombre = int(nombre)
            erreur = 0
        except ValueError:
            nombre = input("Erreur. Veuillez entrer un nombre entier : ")
    return nombre