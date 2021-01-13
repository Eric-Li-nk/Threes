def get_user_move():
    """
    Saisi et retourne le coup joué par le joueur parmi les choix :
    returne Choix de l'utilisateur ( en minuscule )
    
    - "h" pour haut,
    - "b" pour bas,
    - "d" pour droite,
    - "g" pour gauche,
    - "m" pour menu principal.
    """
    saisie = input("Choississez une direction de déplacement ou le menu principal ( Valeur accepté : h,b,d,g,m ) : ")
    saisie = saisie.lower()
    while saisie != "h" and saisie != "b" and saisie != "d" and saisie != "g" and saisie != "m":
        saisie = input("Saisissez une valeur valable ( Valeur accepté : h,b,d,g,m ) : ")
        saisie = saisie.lower()
    return saisie

def get_user_menu(partie):
    """
    Saisi et retourne le choix du joueur dans le menu principal
    param partie : Partie du jeu en cours ou None sinon
    return Choix de l'utilisateur ( en majuscule )
    
    - 'N' : Commencer une nouvelle partie,
    - 'L' : Charger une partie,
    - 'S' : Sauvegarder la partie en cours ( si le paramètre partie correspond à une partie en cours )
    - 'C' : Reprendre la partie en cours ( si le paramètre partie correspond à une partie en cours )
    - 'Q' : Terminer le jeu.
    """
    if partie == None:
        saisie = input("New game - Load game - Quit ( Valeur accepté : N,L,Q ) : ")
        saisie = saisie.upper()
        while saisie != "N" and saisie != "L" and saisie != "Q":
            saisie = input("Saisissez une valeur valable ( Valeur accepté : N,L,Q ) : ")
            saisie = saisie.upper()
    else:
        saisie = input("New game - Load game - Save - Continue - Quit ( Valeur accepté : N,L,S,C,Q ) : ")
        saisie = saisie.upper()
        while saisie != "N" and saisie != "L" and saisie != "S" and saisie != "C" and saisie != "Q":
            saisie = input("Saisissez une valeur valable ( Valeur accepté : h,b,d,g,m ) : ")
            saisie = saisie.upper()
    return saisie