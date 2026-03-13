def __init__(self, name, population, gold):
    self.name = name
    self.population = population
    self.gold = gold
    pass


def plunder(self, people, gold):
    self.population -= people
    self.gold -= gold
    print(f"{self.name} plundered! {gold} gold stolen, {people} citizens killed.")
    if self.gold <= 0 or self.population <= 0:
        print(f"{self.name} has been wiped off the map!")
        return True
    return False
    pass


def prosper(self, gold):
    if gold < 0:
        print("Gold added cannot be a negative number!")
        return
    else:
        self.gold += gold
        print(f"{gold} gold added to the city treasury. {self.name} now has {self.gold} gold.")
    pass


towns = {}

while True:
    line = input()
    if line == "Sail":
        break

    name, population, gold = line.split("||")
    current_population = int(population)
    current_gold = int(gold)
    if name in towns:
        towns[name].population += current_population
        towns[name].gold += current_gold
    else:
        towns[name] = Town(name, current_population, current_gold)
    pass

while True:
    command = input()
    if command == "End":
        break

    parts = command.split("=>")
    action = parts[0]
    town_name = parts[1]
    if action == "Plunder":
        peoples = int(parts[2])
        goldies = int(parts[3])
        should_delete = towns[town_name].plunder(peoples, goldies)
        if should_delete:
            del towns[town_name]

    elif action == "Prosper":
        gold = int(parts[2])
        towns[town_name].prosper(gold)

    pass

if towns:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to: ")
    for town in towns.values():
        print(f"{town.name} -> Population: {town.population} citizens, Gold: {town.gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")