spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food['name'])
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food['heat_level']
        print(f"{food['name']} - Cuisine: {food['cuisine']} - Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_foods_by_cuisine = []
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            spicy_foods_by_cuisine.append(food)
    return spicy_foods_by_cuisine

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food['heat_level']
        print(f"{food['name']} - Heat Level: {heat_level_emojis}")

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food['heat_level'] for food in spicy_foods)
    if len(spicy_foods) > 0:
        average_heat_level = total_heat_level / len(spicy_foods)
        return average_heat_level
    else:
        return 0

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

# Example usage
spicy_food_to_add = {
    "name": "Volcano Ramen",
    "cuisine": "Japanese",
    "heat_level": 8,
}
create_spicy_food(spicy_foods, spicy_food_to_add)

print("Spicy food names:", get_names(spicy_foods))
print("Spiciest foods:")
print_spiciest_foods(get_spiciest_foods(spicy_foods))
print("Average heat level:", get_average_heat_level(spicy_foods))
