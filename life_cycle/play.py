from game.play import *
import life_cycle
from tiles.tiles_moves import *
from tiles.tiles_acces import *
from ui.play_display import *
from life_cycle.play import *
from ui.user_entries import *

def cycle_play(partie):
    """ Permet de jouer à Threes
        param partie : Partie de jeu en cours ou None sinon
        return True si la partie est terminée, False si menu demandé
        
        Séquencement des actions pour cette fonction :
        1 - afficher le plateau de jeu,
        2 - affiche la prochaine tuile pour informer le joueur
        3 - saisir le mouvement proposé par le joueur ; deux cas possible :
            * jouer le coup du joueur courant, mettre à jour le score et revenir au point 1
            * ou retourner False si menu demandé
        4 - si la partie est terminée, retourne True
    """
    if partie == None:
        partie = create_new_play()
    # Séquence 1 : affiche le plateau du jeu
    medium_display(partie["plateau"])
    # Séquence 2 : affiche la prochaine tuile
    tuile = partie["next_tile"]
    while tuile["check"]:
        
        val_tuile = tuile["0"]["val"]
        print("Valeur de la prochaine tuile :", val_tuile)
        saisie = get_user_move()
        if saisie == "m" : # Menu choisie
            return partie
        else: # Déplacement choisie
            play_move(partie["plateau"], saisie) # Déplacement des tuiles
            tuile = get_next_alea_tiles(partie["plateau"],"encours") # Obtiens une val entre 1 et 3
            if get_nb_empty_rooms(partie["plateau"]) != 0: # Si le plateau contient une case libre, remplace la case libre par la nouvelle tuile
                tuile["0"]["val"] = val_tuile # On change les coordonnées après le mouvement car risque de remplacer une case non libre sinon
                put_next_tiles(partie["plateau"],tuile)
            partie["score"] = life_cycle.cycle_game.get_score(partie["plateau"]) # Mise à jour du score
            medium_display(partie["plateau"]) # Affiche plateau
            tuile = get_next_alea_tiles(partie["plateau"],"encours") # Obtiens une val entre 1 et 3
            partie["next_tile"] = tuile # Mise à jour de la tuile à mettre ensuite
            
    print("vous avez perdu ! Score :",partie["score"]) # Fin de la partie
    return True

def save_game(partie):
    """ Sauvegarde une partie dans le fichier game_saved.json"""
    fichier = open("save/save_game.json","w")
    json.dump(partie, fichier, indent = 4)
    fichier.close()
    print("Votre partie a été sauvegardé.")
    
def restore_game():
    """ Restaure et retourne une partie sauvegardée dans le
    fichier "saved_game.json" , ou retourne une nouvelle
    partie si aucune partie n'est sauvegardée
    """
    fichier = open("save/save_game.json","r")
    partie = json.loads(fichier.read())
    fichier.close()
    return partie