
pokemon_team = [
    {"name": "Pikachu", "type": "Electric", "level": 25},
    {"name": "Charizard", "type": "Fire/Flying", "level": 36},
    {"name": "Bulbasaur", "type": "Grass/Poison", "level": 15},
    {"name": "Squirtle", "type": "Water", "level": 18},
    {"name": "Gengar", "type": "Ghost/Poison", "level": 30}
]
print("My Pokémon team:", pokemon_team)

output = ','.join(pokemon['name'] for pokemon in pokemon_team)
print("Pokémon names joined my team:", output)

def view_team():
    print("Current Pokémon team:", pokemon_team)


def add_pokemon():
    new_pokemon = {
        "name": input("Enter the name of the new Pokémon: "),
        "type": input("Enter the type of the new Pokémon: "),
        "level": int(input("Enter the level of the new Pokémon: "))
    }
    pokemon_team.append(new_pokemon)

    print(f"{new_pokemon} has been added to your team.")

add_pokemon()
view_team()
print(pokemon_team)

