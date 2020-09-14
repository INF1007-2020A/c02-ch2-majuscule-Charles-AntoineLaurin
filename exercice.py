#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    lettre = ''
    for lettre in mot:
        # TODO completer la fonction ici
        chiffre = ord(lettre) - 32
        resultat += chr(chiffre)

    return resultat
        
    
  

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
