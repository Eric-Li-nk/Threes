from tiles.tiles_acces import *
import life_cycle
from random import *

def get_nb_empty_rooms(plateau):
    nb_cases_libres = 0
    i = 0
    while i < len(plateau["tiles"]):
        if plateau["tiles"][i] == 0:
            nb_cases_libres += 1
        i += 1
    plateau['nb_cases_libres'] = nb_cases_libres
    return nb_cases_libres

def get_next_alea_tiles(plateau,mode):
    """Retourne une ou deux tuiles(s) dont la disposition (ligne,colonne) est tirée 
       aléatoirement et correspond à un emplacement libre du plateau"""
      
    # Teste si le mode est bien définit c-à-d deux modes sont possibles 'init' et 'encours'
    assert mode in ['init' ,'encours'], "Deux modes sont possibles 'init' et 'encours' (voir commentaire de la fonction)"
    if mode=='init':
        #En mode 'init' deux valeurs sont introdiutes dans le plateau
        # Création d'un tableau de 16 case  dont les valeurs sont ceux des indices du tableau tile dans le plateau
        tableau=list(range(16))
        # On prend aléatoirement un premier indice stocké dans un variable x
        x=randint(0,15)
        # On supprime cette valeur dans le tableau pour ne pas le reprendre
        del(tableau[x])
        # On prend aléatoirement un deuxième indice dans le tableau stocké dans un variable i
        i=randint(0,14)
        # On prend aléatoirement un premier indice stocké dans un variable x
        y=tableau[i]
        # Pour accéder aux cases: l'indice de la ligne est la division entière et la colonne reste de la division
        return {'mode':'init', "0":{'val':2,'ligne':x//4,'colonne':x%4}, "1":{'val':1,'ligne':y//4,'colonne':y%4},
              'check': not life_cycle.cycle_game.is_game_over(plateau)}
    else:
        # En mode 'encours' On récupère les indices du tableau tiles ayant la valeur 0 
        tableau=[]
        for i in range(16):
            if plateau['tiles'][i]==0:
                tableau.append(i)
        if len (tableau)!=0:
            # S'il y a au moins une case libre, on choisi de manière aléatoire une de ces valeurs du tableau crée
            indice = randint(0,len(tableau)-1)
            x, val = tableau[indice], randint(1,3)
            return {'mode':'encours',"0":{'val':val,'ligne':x//4,'colonne':x%4},'check': not life_cycle.cycle_game.is_game_over(plateau)}
        # Si ya pas de case vide on passe
        else:
            return {'mode':'encours',"0":{'val':randint(1,3),'ligne':None,'colonne':None},'check': not life_cycle.cycle_game.is_game_over(plateau)}

def put_next_tiles(plateau,tiles):
    """Permet de placer une ou deux tuiles dans les plateau"""
    if tiles["mode"] == 'init':
        val1 = tiles["0"]
        val2 = tiles["1"]
        plateau["tiles"][val1['ligne']*plateau['n']+val1["colonne"]] = val1["val"]
        plateau["tiles"][val2['ligne']*plateau['n']+val2["colonne"]] = val2["val"]
    else:
        val1 = tiles["0"]
        plateau["tiles"][val1['ligne']*plateau['n']+val1["colonne"]] = val1["val"]

def line_pack(plateau,num_ligne,debut,sens):
    """Tasse les tuiles d'une ligne dans un sens donné
       plateau : dictionnaire contenant le plateau du jeu
       num_ligne : indice de la ligne à "tasser"
       debut : indice à partir duquel se fait le "tassement"
       sens : du "tassement, 1 vers la gauche, 0 vers la droite
    """
    
    assert debut < plateau["n"] and debut >= 0
    assert num_ligne < plateau["n"] and num_ligne >= 0
    
    if sens == 0:
        
        while debut > 0:
            plateau["tiles"][ num_ligne * plateau["n"] + debut ] = plateau["tiles"][ num_ligne * plateau["n"] + debut - 1 ]
            debut -= 1
        plateau["tiles"][ num_ligne * plateau["n"] + debut ] = 0
        
    elif sens == 1:
        
        while debut < plateau["n"] - 1:
            plateau["tiles"][ num_ligne * plateau["n"] + debut ] = plateau["tiles"][ num_ligne * plateau["n"] + debut + 1 ]
            debut += 1
        plateau["tiles"][ num_ligne * plateau["n"] + debut ] = 0
        
            
def colum_pack(plateau, num_col, debut, sens):
    """Tasse les tuiles d'une colonne dans un sens donné
       plateau : dictionnaire contenant le plateau du jeu
       num_col : indice de la colonne à "tasser"
       debut : indice à partir duquel se fait le "tassement"
       sens : du "tassement, 1 vers le haut, 0 vers le bas
    """
    
    assert debut < plateau["n"] and debut >= 0
    assert num_col < plateau["n"] and num_col >= 0
    
    if sens == 0:
        
        while debut > 0:
            plateau["tiles"][ debut * plateau["n"] + num_col ] = plateau["tiles"][ (debut - 1) * plateau["n"] + num_col ]
            debut -= 1
        plateau["tiles"][ debut * plateau["n"] + num_col ] = 0
        
    elif sens == 1:
        
        while debut < plateau["n"] - 1:
            plateau["tiles"][ debut * plateau["n"] + num_col ] = plateau["tiles"][ (debut + 1) * plateau["n"] + num_col ]
            debut += 1
        plateau["tiles"][ debut * plateau["n"] + num_col ] = 0
            
def line_move(plateau, num_lig, sens):
    """ Déplacement des tuiles d'une ligne donnée dans un sens donné 
        en appliquant les règles du jeu Threes
        plateau : dictionnaire contennant le plateau du jeu
        num_lig : indice de la ligne pour laquelle il faut déplacer
                  les tuiles
        sens : sens du déplacement des tuiles, 1 vers la gauche, 0 vers la droite
    """
    assert sens == 1 or sens == 0
    
    p_longueur = plateau["n"] - 1
    
    if sens == 0 :
        
        num_col = p_longueur
        if is_room_empty(plateau, num_lig, num_col) == False:
            while num_col > 0 and is_room_empty(plateau, num_lig, num_col - 1) == False :
                tile_1 = get_value(plateau, num_lig, num_col)
                tile_2 = get_value(plateau, num_lig, num_col - 1)
                if tile_1 == 1 and tile_2 == 2 or tile_1 == 2 and tile_2 == 1:
                    line_pack(plateau, num_lig, num_col, 0)
                    set_value(plateau, num_lig, num_col, 3)
                elif tile_1 == tile_2 and tile_1 != 1 and tile_1 != 2 :
                    line_pack(plateau, num_lig, num_col, 0)
                    set_value(plateau, num_lig, num_col, tile_1 * 2)
                num_col -= 1
                
        num_col = 0
        while num_col <= p_longueur and is_room_empty(plateau, num_lig, num_col):
            num_col += 1
        while num_col <= p_longueur:
            while is_room_empty(plateau, num_lig, num_col):
                line_pack(plateau, num_lig, num_col, 0)
            num_col += 1
            
    else:
        
        num_col = 0 
        if is_room_empty(plateau, num_lig, num_col) == False:
            while num_col < p_longueur and is_room_empty(plateau, num_lig, num_col + 1) == False :
                tile_1 = get_value(plateau, num_lig, num_col)
                tile_2 = get_value(plateau, num_lig, num_col + 1)
                if tile_1 == 1 and tile_2 == 2 or tile_1 == 2 and tile_2 == 1:
                    line_pack(plateau, num_lig, num_col, 1)
                    set_value(plateau, num_lig, num_col, 3)
                elif tile_1 == tile_2 and tile_1 != 1 and tile_1 != 2:
                    line_pack(plateau, num_lig, num_col, 1)
                    set_value(plateau, num_lig, num_col, tile_1 * 2)
                num_col += 1
        
        num_col = p_longueur
        while num_col >= 0 and is_room_empty(plateau, num_lig, num_col):
            num_col -= 1        
        while num_col >= 0:
            while is_room_empty(plateau, num_lig, num_col):
                line_pack(plateau, num_lig, num_col, 1)
            num_col -= 1

def column_move(plateau, num_col, sens):
    """ Déplacement des tuiles d'une colonne donnée dans un sens donné
        en appliquant les règles du jeu Threes
        plateau : dictionnaire contenant le plateau du jeu
        num_col : indice de la colonne pour laquelle il faut déplacer les tuiles
        sens : sens du déplacement des tuiles, 1 vers le haut, 0 vers le bas
        
    """
    assert sens == 1 or sens == 0
    
    p_largeur = plateau["n"] - 1
    
    if sens == 0 :
        
        num_lig = p_largeur
        if is_room_empty(plateau, num_lig, num_col) == False:
            while num_lig > 0 and is_room_empty(plateau, num_lig - 1, num_col) == False :
                tile_1 = get_value(plateau, num_lig, num_col)
                tile_2 = get_value(plateau, num_lig - 1, num_col)
                if tile_1 == 1 and tile_2 == 2 or tile_1 == 2 and tile_2 == 1:
                    colum_pack(plateau, num_col, num_lig, 0)
                    set_value(plateau, num_lig, num_col, 3)
                elif tile_1 == tile_2 and tile_1 != 1 and tile_1 != 2 :
                    colum_pack(plateau, num_col, num_lig, 0)
                    set_value(plateau, num_lig, num_col, tile_1 * 2)
                num_lig -= 1
                
        num_lig = 0
        while num_lig <= p_largeur and  is_room_empty(plateau, num_lig, num_col):
            num_lig += 1
        while num_lig <= p_largeur:
            while is_room_empty(plateau, num_lig, num_col):
                colum_pack(plateau, num_col, num_lig, 0)
            num_lig += 1
            
    else:
        
        num_lig = 0 
        if is_room_empty(plateau, num_lig, num_col) == False:
            while num_lig < p_largeur and is_room_empty(plateau, num_lig + 1, num_col) == False :
                tile_1 = get_value(plateau, num_lig, num_col)
                tile_2 = get_value(plateau, num_lig + 1, num_col)
                if tile_1 == 1 and tile_2 == 2 or tile_1 == 2 and tile_2 == 1:
                    colum_pack(plateau, num_col, num_lig, 1)
                    set_value(plateau, num_lig, num_col, 3)
                elif tile_1 == tile_2 and tile_1 != 1 and tile_1 != 2:
                    colum_pack(plateau, num_col, num_lig, 1)
                    set_value(plateau, num_lig, num_col, tile_1 * 2)
                num_lig += 1
        
        num_lig = p_largeur
        while num_lig >= 0 and is_room_empty(plateau, num_lig, num_col):
            num_lig -= 1        
        while num_lig >= 0:
            while is_room_empty(plateau, num_lig, num_col):
                colum_pack(plateau, num_col, num_lig, 1)
            num_lig -= 1
            
def lines_move(plateau, sens):
    """ Déplace les tuiles de toutes les lignes du plateau
        dans un sens donné en appliquant les règles du jeu Threes
        plateau : dictionnaire contenant le plateau du jeu
        sens : sens du déplacement; 1 vers la gauche, 0 vers la droite
    """
    i = 0
    while i < plateau["n"]:
        line_move(plateau, i, sens)
        i += 1
        
def columns_move(plateau, sens):
    """ Déplace les tuiles de toutes les colonnes du plateau
        dans un sens donné en appliquant les règles du jeu Threes
        plateau : dictionnaire contenant le plateau du jeu
        sens : sens du déplacement; 1 vers le haut, 0 vers le bas
    """
    i = 0
    while i < plateau["n"]:
        column_move(plateau, i, sens)
        i += 1
        
def play_move(plateau, sens):
    """ Déplace les tuiles du plateau dans un sens donné en
        appliquant les règles du jeu Threes
        plateau : plateau de jeu
        sens : sens de déplacement des tuiles
    """
    if sens == "b":
        columns_move(plateau,0)
    elif sens == "h":
        columns_move(plateau,1)
    elif sens == "d":
        lines_move(plateau, 0)
    elif sens == "g":
        lines_move(plateau, 1)
    else:
        print("'sens' ne contient pas une bonne valeur.")
    
