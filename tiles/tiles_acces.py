def check_indice(plateau, indice):
    """Retourne True si indice correspond à un indice valide de case pour le plateau (entre 0 et n-1)"""
    return indice <= plateau["n"] - 1 and indice >= 0 

def check_room(plateau, ligne, colonne):
    """Retourne True si (ligne,colonne) est une case du plateau (ligne et colonne sont des indices valides)"""
    return check_indice(plateau,ligne) and check_indice(plateau,colonne)

def get_value(plateau,ligne,colonne):
    """Retourne la valeur de la case (ligne,colonne) Erreur si (ligne,colonne) n'est pas valide"""
    return plateau['tiles'][colonne + ligne * plateau['n']]

def set_value(plateau,ligne,colonne,valeur):
    """Affecte la valeur 'valeur' dans la case (ligne,colonne) du plateau Erreur si (ligne,colonne) n'est pas une case valide 
       ou si valeur n'est pas supérieure ou égal à 0
       Met aussi à jour le nombre de cases libres (sans tuile(s))"""
    plateau['tiles'][colonne + ligne * plateau['n']] = valeur

def is_room_empty(plateau,ligne,colonne):
    """Teste si une case du plateau est libre ou pas
       retourne True si la case est libre, False sinon"""
    return get_value(plateau,ligne,colonne) == 0
