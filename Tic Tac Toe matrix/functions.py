
# Student name: Anthony  Daher et Tony Chamoun
# Numéros étudiants: 300233710 et 300238262
# Question 2 - Devoir 5
# Completer les fonctions si dessous pour jouer tic-tac-toe

def effaceTableau(tab):
   '''
   (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice) 
   en mettant '-' dans tous les elements.
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   # a completer
   for i in range(0,3):
      tab.remove(tab[0])
   for i in range(0,3):
      tab.append(['-','-','-'])
   
   # retourne rien

def verifieGagner(tab):  
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!" 
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''

    # a completer
    if testLignes(tab) == 'X':
       print("Joueur X a gagné!")
       return True
    if testCols(tab) == 'X':
       print("Joueur X a gagné!")
       return True
    if testDiags(tab) == 'X':
       print("Joueur X a gagné!")
       return True
    if testLignes(tab) == 'O':
       print("Joueur O a gagné!")
       return True
    if testCols(tab) == 'O':
       print("Joueur O a gagné!")
       return True
    if testDiags(tab) == 'O':
       print("Joueur O a gagné!")
       return True
    if testMatchNul(tab) == True:
       print("Match nul")
       return True
    return False# a changer

 
def testLignes(tab):
   ''' (list) ->  str
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer
   for i in tab:
      if i == ['O','O','O']:
         return 'O'
      if i == ['X','X','X']:
         return 'X'
   return '-' # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant 
  
def testCols(tab):
   ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
   # a completer
   c = len(tab)
   r = len(tab[0])
   for i in range(0,c):
      colonne = []
      for j in range(0,r):
         x = tab[j][i]
         colonne.append(x)
      if colonne == ['O','O','O']:
         return 'O'
      if colonne == ['X','X','X']:
         return 'X'
   return '-'   #a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

def testDiags(tab):
   ''' (list) ->  str
   * cherche trois 'X' ou trois 'O' dans une diagonale.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer
   diag = []
   for j in range(0,3):
      x = tab[j][j]
      diag.append(x)
   if diag == ['O','O','O']:
      return 'O'
   if diag == ['X','X','X']:
      return 'X'
   diag = []
   i = 0
   for j in range(2,-1,-1):
      x = tab[j][i]
      diag.append(x)
      i+=1
   if diag == ['O','O','O']:
      return 'O'
   if diag == ['X','X','X']:
      return 'X'
   else:
      return '-'   # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant
  
def testMatchNul(tab):
   ''' (list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
   * Si on ne trouve pas de '-' dans la matrice, retourne True. 
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer
   c = len(tab)
   r = len(tab[0])
   for i in range(0,c):
      colonne = []
      for j in range(0,r):
         x = tab[j][i]
         if x == '-':
            return False
   return True  # a changer
