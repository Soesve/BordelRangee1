""" Branche dev ajout fizzbuzz

    Returns:
        _type_: int
"""

print("Hello la team")


#création d'une structure conditionnelle dans une liste de 1 à  36 verifier si le nombre est un multiple de 3 et/ou de 5
def fizzBuzz():
    """ Méthode permettant de mettre en place le celèbre FizzBuzz 
    return : None
    """
    for i in range(1,36) :
        if  i %3 == 0 and i %5 ==0 : #verifier si le nombre est un multiple de 3 et de 5 ou 
            # i%15 == 0
            print ("FizzBuzz!") # afficher fizzBuzz si oui 
            
        elif i %3 == 0 :
        # affichage print() du mot "Fizz!" si cond précédente ok 
            print ("Fizz!") # sinon si multiple de 3 afficher Fizz!

        elif i %5 ==0 :
        # affichage  print() du mot "Buzz!" si cond précédente ok 
            print("Buzz!") # sinon si multiple de 5 afficher Buzz!

        # sinon affichage du nombre
        else : 
            print(i) # sinon afficher le nombre 
fizzBuzz()