def render(scene):
    letters:str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ  "
    print("    "+"   ".join(letters[:len(scene)]))
    """
    enumeration des coordonnées sur l'axe Y avec l'ajout des des bons espacements
    """
    for i, p in enumerate(scene, 1):
        for j, cell in enumerate(p):
            if cell != "~" and cell != "x":
                p[j] = "o"

        """
          Calcul de la longueur totale de la ligne, en incluant les séparateurs
        """
        line_length = len(p) * 4 + 2
        """
        bonne longueur de ligne
        """
        """
        Création de la ligne de séparation
        """
        separator = '-' * line_length
        print(separator)
        if i<10:
            i = "0"+str(i)
        print(f"{i}| {' | '.join(p)} |")
        '''
        creation des colonnes
        '''
    print(separator)
