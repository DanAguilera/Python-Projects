import json
import random
# using this workshop to take an interest and combining that with data structures and file handling. 

pokemon_team = [
    {"name": "Pikachu", 
     "type": "Electric",
     "level": 25,
     "hp": 100,
     "moves": [
         {"name": "Thundershock", "type": "Electric", "power": 12},
         {"name": "Quick Attack", "type": "Normal", "power": 10}
     ]
     },
    {"name": "Charizard",
     "type": "Fire/Flying",
     "level": 36,
     "hp": 100,
     "moves": [
         {"name": "Ember", "type": "Fire", "power": 14},
         {"name": "Quick Attack", "type": "Normal", "power": 10}
     ]
     },
    {"name": "Bulbasaur",
     "type": "Grass/Poison",
     "level": 15,
     "hp": 100,
     "moves": [
         {"name": "Ember", "type": "Fire", "power": 14},
         {"name": "Quick Attack", "type": "Normal", "power": 10}
     ]
     },
    {"name": "Squirtle",
     "type": "Water",
     "level": 18,
     "hp": 100,
     "moves": [
         {"name": "Ember", "type": "Fire", "power": 14},
         {"name": "Quick Attack", "type": "Normal", "power": 10}
     ]
     },
    {"name": "Gengar",
     "type": "Ghost/Poison"
     , "level": 30,
     "hp": 100,
     "moves": [
         {"name": "Ember", "type": "Fire", "power": 14},
         {"name": "Quick Attack", "type": "Normal", "power": 10}
     ]
     }
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


# def view_team():
#     for pokemon in pokemon_team:
#         print(f"{pokemon['name']} (Type: {pokemon['type']}, Level: {pokemon['level']}), HP: {pokemon['hp']}")

def view_team():
    #enumerate(..., start=1) is just for displaying a human-friendly number
    for index, pokemon in enumerate(pokemon_team, start=1):
        print(f"Pokemon {index}: {pokemon['name']},  {pokemon['type']}, {pokemon['level']}, {pokemon['hp']}")


def select_pokemon():
    while True:
        view_team()
        choice = int(input("Choose a pokemon you want to use for battle? "))

        if choice < 1 or choice > len(pokemon_team):
            print("Invalid choice. Please select a valid Pokémon number.")
        else:
            pokemon = pokemon_team[choice - 1]
            print(f"You have selected {pokemon['name']}!")
            return pokemon


def add_pokemon():
    new_pokemon = {
        "name": input("Enter the name of the new Pokémon: "),
        "type": input("Enter the type of the new Pokémon: "),
        "level": int(input("Enter the level of the new Pokémon: ")),
        "hp": 100
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



#Attacking and Defending functions 
def attack(attacker, defender, move):
    damage = move["power"]
    crit = random.randint(1,100)
    if crit <= 20:
        damage = damage * 2
        print("CRITICAL HIT")
    defender["hp"] -= damage

    if defender["hp"] < 0:
        defender["hp"] = 0

    print(f"{attacker['name']} attacks {defender['name']} using {move['name']} for {damage} damage!")
    print(f"{defender['name']} now has {defender['hp']} HP left.\n")

def battle(pokemon1, pokemon2):
    print(f"\nA battle starts between {pokemon1['name']} and {pokemon2['name']}!\n")
    
    while pokemon1["hp"] > 0 and pokemon2["hp"] > 0:
        move1 = random.choice(pokemon1["moves"])
        attack(pokemon1, pokemon2, move1)

        if pokemon2["hp"] <= 0:
            print(f"{pokemon2['name']} has fainted!")
            print(f"{pokemon1['name']} wins the battle!\n")
            break
        move2 = random.choice(pokemon2["moves"])
        attack(pokemon2, pokemon1, move2)

        if pokemon1["hp"] <= 0:
            print(f"{pokemon1['name']} has fainted!")
            print(f"{pokemon2['name']} wins the battle!\n")
            break

#Menu loop
    

def menu():
    while True:
        print("\nMenu:")
        print("1. View Pokémon Team")
        print("2. Add a Pokémon")
        print("3. Find a Pokémon")
        print("4. Battle Mode")
        print("5. Remove a Pokémon")
        print("6. Exit")

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
            pokemon1 = select_pokemon()
            pokemon2 = select_pokemon()
            
            while pokemon1 == pokemon2:
                print("You cannot battle the same Pokémon. Please select a different one.")
                pokemon2 = select_pokemon()

            battle(pokemon1, pokemon2)
        elif choice == "5":
            remove_pokemon()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


load_team()
menu()



