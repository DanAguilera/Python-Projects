import json
# using this workshop to take an interest and combining that with data structures and file handling. 
pokemon_team = [
    {"name": "Pikachu", "type": "Electric", "level": 25},
    {"name": "Charizard", "type": "Fire/Flying", "level": 36},
    {"name": "Bulbasaur", "type": "Grass/Poison", "level": 15},
    {"name": "Squirtle", "type": "Water", "level": 18},
    {"name": "Gengar", "type": "Ghost/Poison", "level": 30}
]

print("My Pokémon team:", pokemon_team)
# 'w' is for write, 'r' is for read, 'a' is for append.
output = ", ".join(pokemon["name"] for pokemon in pokemon_team)
print("Pokémon on my team:", output)

def save_team():
    with open("pokemon_team.json", "w") as file:
        json.dump(pokemon_team, file)

def load_team():
    global pokemon_team
    try:
        with open("pokemon_team.json", "r") as file:
            pokemon_team = json.load(file)
    except FileNotFoundError:
        print("No saved team found. Starting fresh.")




def view_team():
    for pokemon in pokemon_team:
        print(f"{pokemon['name']} (Type: {pokemon['type']}, Level: {pokemon['level']})")


def add_pokemon():
    new_pokemon = {
        "name": input("Enter the name of the new Pokémon: "),
        "type": input("Enter the type of the new Pokémon: "),
        "level": int(input("Enter the level of the new Pokémon: "))
    }
    pokemon_team.append(new_pokemon)
    print(f"{new_pokemon['name']} has been added to your team.")
    save_team()


def find_pokemon():
    search = input("Enter the name, type, or level of the Pokémon you want to find: ")
    
    for pokemon in pokemon_team:
        if pokemon["name"].lower() == search.lower():
            return pokemon
        elif pokemon["type"].lower() == search.lower():
            return pokemon
        elif search.isdigit() and pokemon["level"] == int(search):
            return pokemon
    
    return None

def remove_pokemon():
    selection = input("Enter the name of the Pokémon you want to remove: ")
    for pokemon in pokemon_team:
        if pokemon['name'].lower() == selection.lower():
            pokemon_team.remove(pokemon)
            print(f"{pokemon['name']} has been removed from your team.")
            save_team()
            return

    print(f"{selection} is not in your team.")
    

def menu():
    while True:
        print("\nMenu:")
        print("1. View Pokémon Team")
        print("2. Add a Pokémon")
        print("3. Find a Pokémon")
        print("4. Remove a Pokémon")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_team()
        elif choice == "2":
            add_pokemon()
        elif choice == "3":
            result = find_pokemon()
            if result:
                print(f"Found Pokémon: {result['name']} (Type: {result['type']}, Level: {result['level']})")
            else:
                print("Pokémon not found in the team.")
        elif choice == "4":
            remove_pokemon()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


load_team()
menu()



