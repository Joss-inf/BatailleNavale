def render(scene):


    letters:str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ  "
    print("   "+"   ".join(letters[:len(scene)]))
    for i, p in enumerate(scene, 1):
        """
          Calcul de la longueur totale de la ligne, en incluant les séparateurs
        """
        line_length = len(p) * 4 + 2
        """"
         4 caractères par élément + 2 pour les bords
        Création de la ligne de séparation
        """
        separator = '-' * line_length
        print(separator)
        if i<10:
            i = "0"+str(i)
        print(f"{i}| {' | '.join(p)} |")
    print(separator)