import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
"""
Construis le chemin complet de ce  fichier
"""
json_file_path = os.path.join(current_dir, '../data/config.json')
"""
Obtiens le chemin absolu du répertoire courant
"""
try:
    with open(json_file_path,"r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Le fichier config.json n'a pas été trouvé.")
except json.JSONDecodeError:
    print("Le fichier config.json contient des erreurs de syntaxe JSON.")
"""
On charge le Json avec un try et des retours d'erreur
"""
def GetJsonParse():
    return data
"""
on fais un get pour obtenir les data quand on exportera la fonction
"""

"O(n)"