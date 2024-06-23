import sqlite3
import json

# Load JSON data from a file with the correct encoding
with open('recipes.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Connect to SQLite database (or create it)
conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS cocktails (
    id INTEGER PRIMARY KEY,
    name TEXT,
    glass TEXT,
    category TEXT,
    garnish TEXT,
    preparation TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY,
    cocktail_id INTEGER,
    unit TEXT,
    amount REAL,
    ingredient TEXT,
    label TEXT,
    FOREIGN KEY (cocktail_id) REFERENCES cocktails(id)

)
''')

# Insert JSON data into the tables
for cocktail in data:
    name = cocktail.get('name', 'Unnamed')
    glass = cocktail.get('glass', 'Unknown glass')
    category = cocktail.get('category', 'Uncategorized')  # Provide a default value if 'category' key is missing
    garnish = cocktail.get('garnish', 'No garnish')       # Provide a default value if 'garnish' key is missing
    preparation = cocktail.get('preparation', 'No preparation') # Provide a default value if 'preparation' key is missing
    cursor.execute('''
    INSERT INTO cocktails (name, glass, category, garnish, preparation)
    VALUES (?, ?, ?, ?, ?)
    ''', (name, glass, category, garnish, preparation))
    cocktail_id = cursor.lastrowid

    for ingredient in cocktail['ingredients']:
        unit = ingredient.get('unit', 'unknown')          # Provide a default value if 'unit' key is missing
        amount = ingredient.get('amount', 0)              # Provide a default value if 'amount' key is missing
        ingredient_name = ingredient.get('ingredient', 'unknown')  # Provide a default value if 'ingredient' key is missing
        label = ingredient.get('label', None)             # Handle the 'label' key, default to None
        cursor.execute('''
        INSERT INTO ingredients (cocktail_id, unit, amount, ingredient, label)
        VALUES (?, ?, ?, ?, ?)
        ''', (cocktail_id, unit, amount, ingredient_name, label))

# Commit changes and close connection
conn.commit()
conn.close()

print("Data loaded successfully from JSON file into SQLite database.")