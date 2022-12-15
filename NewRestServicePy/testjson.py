import json

with open("input.json") as entree_json:
    entree_data = json.load(entree_json)

    print("Type:", type(entree_data))

    print("\nLibelle:", entree_data["libelle"])
    print("\nScenario:", entree_data["TypeScenario"])
    print("\nParametre 1:", entree_data["Parametres"][0])
    print("\nParametre 1:", entree_data["Parametres"][0])
