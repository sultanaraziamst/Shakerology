# Connect to SQLite database
import sqlite3

conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()

# Query the cocktail data
cursor.execute('SELECT * FROM cocktails')
cocktails = cursor.fetchall()

for cocktail in cocktails:
    print(f"Cocktail: {cocktail}")
    cursor.execute('SELECT * FROM ingredients WHERE cocktail_id = ?', (cocktail[0],))
    ingredients = cursor.fetchall()
    for ingredient in ingredients:
        print(f"  Ingredient: {ingredient}")

# Close connection
conn.close()