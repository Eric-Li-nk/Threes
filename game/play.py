import sys
import json
sys.path.append("../")
from tiles.tiles_moves import *
from tiles.tiles_acces import *
from life_cycle.cycle_game import *

def init_play():
    """Retourne un plateau correspondant à une nouvelle partie
    Une nouvelle partie est un dictionnaire avec les clefs et valeurs suivantes :
    - 'n' : vaut 4
    - 'nb_cases_libres' : 16 au départ
    - 'tiles' : tableau de 4*4 cases initialisées à 0
    """
    return {'n':4,'nb_cases_libres':16,'tiles':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}

def create_new_play():
    """
    Créer et retourne une nouvelle partie
    """
    p = init_play()
    put_next_tiles(p,get_next_alea_tiles(p,"init")) 
    tile = get_next_alea_tiles(p,"encours")
    return {"plateau": p,"next_tile": tile, "score": get_score(p)}