import sqlite3

def get_cocktail_recipe(cocktail_name):
    """Function to retrieve recipe for a given cocktail name."""
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    # Perform a case-insensitive search for the cocktail name
    cursor.execute('''
        SELECT ingredient 
        FROM ingredients 
        WHERE cocktail_id = (SELECT id FROM cocktails WHERE LOWER(name) = LOWER(?))
    ''', (cocktail_name,))
    ingredients = cursor.fetchall()

    conn.close()
    return [ingredient[0] for ingredient in ingredients] if ingredients else None

def display_recipe(cocktail_name, ingredients):
    """Function to display recipe for a given cocktail."""
    if ingredients:
        print(f"Recipe for {cocktail_name}:")
        for ingredient in ingredients:
            print(f" {ingredient}")
    else:
        print(f"Sorry, recipe for '{cocktail_name}' not found. Please try again.")

def main():
    print("Welcome to the Shakerology app!")
    while True:
        cocktail_name = input("Enter the name of the Cocktail (or 'quit' to exit):").strip()

        if cocktail_name.lower() == 'quit':
            print("Exiting the app. Cheers!")
            break

        recipe = get_cocktail_recipe(cocktail_name)
        display_recipe(cocktail_name, recipe)

if __name__ == "__main__":
            main()