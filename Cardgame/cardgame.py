

#Question 5 - Devoir 4
# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''

     
     donneur=[]
     autre=[]

     #####################
     x = 1
     for i in range(0,len(p)):
         if x == 1:
             autre += p[i:i+1]
             x = 2
             continue
         if x == 2:
             donneur += p[i:i+1]
             x = 1
     #####################
     return (donneur, autre)
    

def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]

    #####################
    liste = []
    liste2 = []

    for i in range(0,len(l)):
        x = l[i]
        y = len(x)
        if y == 2:
            z = x[0]
            liste += z
            liste2 += z
        if y == 3:
            liste.append('10')
            liste2.append('10')
    
    for i in range(0,len(liste2)):
        c = liste.count(liste2[i])
        if c == 2 or c == 4:
            continue
        if c == 3:
            liste.remove(liste2[i])
            resultat += l[i:i+1]
        else:
            resultat += l[i:i+1]

    #####################

    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''

    #####################

    s2 = ''
    for ch in p[:len(p)-1]:
        s2 += ch + ' '
    s2 += p[len(p)-1]
    return print(s2)

    #####################
    

def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
     '''

     #####################
     if n == 1:
         print("J'ai", n, "cartes. Si 1 est la position de ma première carte et")
         print(n, "la position de ma dernière carte, laquelle de mes cartes voulez-vous?")
         y = 0
         print("SVP entrez un entier de 1 à 1:", end ="")
         y = int(input())
         while y != 1:
             print("Position invalide. SVP entrez un entier de 1 à "+ str(n) +': ', end ="")
             y = int(input())
         print("Vous avez demandé ma 1ère carte.")
         return 0
        
     print("J'ai", n, "cartes. Si 1 est la position de ma première carte et")
     print(n, "la position de ma dernière carte, laquelle de mes cartes voulez-vous?")
     y = 0
     print("SVP entrez un entier de 1 à "+ str(n) +': ', end ="")
     y = int(input())
     while y not in range(1,n+1):
         print("Position invalide. SVP entrez un entier de 1 à "+ str(n) +': ', end ="")
         y = int(input())
     if y == 1: 
         y = str(y)
         print("Vous avez demandé ma "+y+"ère carte.")
     else:
         y = str(y)
         print("Vous avez demandé ma "+y+"ème carte.")
     return int(y)      
      
     #####################


#####################

def alternate(d, h, x):
    if x == 0:
        print("***********************************************************")
        print("Votre tour.")
        print("Votre main est:")
        return h
    if x == 1:
        print("***********************************************************")
        print("Mon tour.")
        if len(h)== 1:
            print("J'ai pris votre 1ère carte.")
            return d,''
        y = random.randint(1,len(h)-1)
        if y == 1:
            d.append(h[0])
            h.remove(h[0])
            print("J'ai pris votre 1ère carte.")
            if len(d) == 0:
                return '', h
            return d, h
            
        else:
            y = str(y)
            print("J'ai pris votre "+ y+"ème carte.")
            y = int(y)
            d.append(h[y-1])
            h.remove(h[y-1])
            if len(d) == 0:
                return '', h
            return d, h

def eliminate(l, h, y):
    x = l[y-1]
    h.append(x)
    l.remove(x)
    print("La voilà. C'est un", x)
    print("Avec", x, "ajouté, votre main est:")
    return l, h

def winner(d, h):
    if d == '':
        print("J'ai terminé toutes les cartes.")
        print("Vous avez perdu! Moi, Robot, j'ai gagné.")
        return 2
    if h == '':
        print("***********************************************************")
        print("J'ai terminé toutes les cartes.")
        print("Félicitations! Vous, Humain, vous avez gagné.")
        return 2
    else:
        return 1
    
#####################
    
def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)

     #####################

     x = 1
     while x ==1:
         b = 1


         if b == 1:
             j = winner(donneur, humain)
             if j == 2:
                 x = 2
                 continue
             humain = alternate(donneur, humain, 0)
             affiche_cartes(humain)
             f = entrez_position_valide(len(donneur))
             donneur, humain = eliminate(donneur, humain, f)
             affiche_cartes(humain)
             print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main")
             print("est:")
             humain = elimine_paires(humain)
             affiche_cartes(humain)
             attend_le_joueur()
             if f == 0:
                 donneur = ''
                 continue
             b = 2


         if b == 2:
             j = winner(donneur, humain)
             if j == 2:
                 x = 2
                 continue
             donneur, humain = alternate(donneur, humain, 1)
             donneur = elimine_paires(donneur)
             attend_le_joueur()
     
     #####################
	 
# programme principale
joue()

