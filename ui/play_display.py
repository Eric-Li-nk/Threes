def simple_display(plateau):
    """Affichage du tableau de façon simplifié"""
    ui = ''
    num_tuile = 1
    while num_tuile < len(plateau['tiles']) + 1:
        ui += str(plateau['tiles'][num_tuile - 1]).rjust(5)
        if num_tuile % 4 == 0:
            ui += '\n'
        num_tuile += 1
    print(ui)

def medium_display(plateau):
    """Affichage du plateau avec délimitations textuelles des cases"""
    ui = '*****************************\n'
    num_tuile = 1
    while num_tuile < len(plateau['tiles']) + 1:
        ui += "*" + str(plateau['tiles'][num_tuile - 1]).rjust(4) + '  '
        if num_tuile % 4 == 0:
            ui += '*\n*****************************\n'
        num_tuile += 1
    print(ui)

def full_display(plateau):
    """Affichage en couleurs"""