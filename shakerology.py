# Define cocktail data
cocktail_data = {
    "Margarita": ["2 oz Tequila", "1 oz Lime juice", "1 oz Cointreau", "Salt for rimming"],
    "Martini": ["2 oz Gin", "1/2 oz Dry vermouth", "Lemon twist or olive for garnish"],
    "Negroni": ["1 oz Gin", "1 oz Campari", "1 oz Sweet vermouth", "Orange twist or slice for garnish"],
    "Old Fashioned": ["2 oz Bourbon or Rye whiskey", "1 sugar cube or 1/2 oz simple syrup", 
                      "2-3 dashes Angostura bitters", "Orange twist for garnish"],
    "Cosmopolitan": ["1 1/2 oz Vodka", "1 oz Cranberry juice", "1/2 oz Triple sec", "1/2 oz Lime juice"],
}
    # Add more cocktails here

def load_cocktail_data():

    """Function to load cocktail data into memoery."""
    return cocktail_data

def get_cocktail_recipe(cocktail_name):
    """Function to retrive recipe for a given cocktail name."""
    cocktails = load_cocktail_data()
    return cocktails.get(cocktail_name)

def display_recipe(cocktail_name, ingredients):
    """Function to display recipe for a given cocktail."""
    if ingredients:
        print(f"Recipe for {cocktail_name}:")
        for ingredients in ingredients:
            print(f" {ingredients}")
   
