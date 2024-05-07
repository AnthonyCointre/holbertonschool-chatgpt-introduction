#!/usr/bin/python3
import sys

def factorial(n):
        """
        calcul le factoriel d'un nombre donne de maniere recursive

        Description de la fonction:
        cette fonction calcule le factoriel d'un nombre donne d'une maniere recursive.
        Le factoriel d'un nombre n'est le produit de tous les entiers positifs 
        inferieur ou egaux a n.

        Parametres:
        - n : int
        le nombre pour lequel le factoriel doit etre calcule.

        Retours:
        int
        le factoriel du nombre donnee.

        """
        if n == 0:
                return 1
        else:
                return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)