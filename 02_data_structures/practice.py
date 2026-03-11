import copy

pokemon = {
    "name": "Pikachu",
    "stats": {"hp": 100, "attack": 50}
}

shallow = pokemon.copy()
deep = copy.deepcopy(pokemon)

shallow["stats"]["hp"] = 50

print("Original stats:", pokemon["stats"])
print("Shallow stats:", shallow["stats"])
print("Deep stats:", deep["stats"])
print("Original HP:", pokemon["stats"]["hp"])