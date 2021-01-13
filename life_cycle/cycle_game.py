from tiles.tiles_moves import *
from tiles.tiles_acces import *
from ui.play_display import *
from life_cycle.play import *

def is_game_over(plateau):
    """Retourne True si la partie est terminée, False sinon"""
    #S'il y'a au moins une case vide, le jeu n'est pas terminé 
    if get_nb_empty_rooms(plateau)!=0:
        return False
    
    #Alors le plateau est plein on procéde anisi
    else:
        # On verifie d'abord sur les lignes
        #S'il existe deux tuiles qui peuvent se fusionner
        #Dès qu'il en existe la fonction s'arrête et retourne False
        i=0
        while i<4:
            j=0
            while j<3:
                x=get_value(plateau,i,j)
                y=get_value(plateau,i,j+1)
                if (x==1 and y==2) or (x==2 and y==1):
                    return False
                elif x%3==0 and x==y:
                    return False
                j+=1
            i+=1
        # S'il y en a pas on verifie d'abord avec les colonnes
        #C'est la même procédure avec les lignes
        i=0
        while i<4:
            j=0
            while j<3:
                x=get_value(plateau,j,i)
                y=get_value(plateau,j+1,i)
                if (x==1 and y==2) or (x==2 and y==1):
                    return False
                elif x%3==0 and x==y:
                    return False
                j+=1
            i+=1
    return True  

def get_score(plateau):
    """Retourne le score du plateau"""
    score = 0
    i = 0
    while i < len(plateau['tiles']):
        score += plateau['tiles'][i]
        i += 1
    return score