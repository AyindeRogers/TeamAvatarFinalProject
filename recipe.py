import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys
from argparse import ArgumentParser


class Recipe: 
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients.split(",")
    def __str__(self):
        return f"{self.ingredients}"
    
def match(recipeList, user_ing): 
    """
    Checks if the user's ingredients satisfy any of the recipes in the 
    textfile by implementing a set intersection. If not, it returns the 
    ingredients the user needs to complete the recipes stored in the
    textfile, through a symmetric difference.
            
    Args: 
        recipeList (str) : stores list of recipes 
        user_ing (set of strings) : contains user's ingredients 
                
    Returns: 
        Match (set of strings): Recipe(s) a user has the correct 
        ingredients for 
        (set of strings): Ingredients a user needs to 
        complete the recipes stored in the filepath. 
    """
        
    user = user_ing.split(",")
    user_ingredients = set(user)  
    
    for r in recipeList:
        
        recipe,ingredients = [r.name, r.ingredients] 
        rec_ing = set(r.ingredients)
        match = user_ingredients & rec_ing
        if match and len(match) == len(rec_ing):
            print(f"You can make {r.name}")
        
        
        else: 
            print(f"""None of your ingredients match our recipes. Here are 
            some ideas to get you started.
            {r.name} = {rec_ing - match}""")
               
    
    
def allergies(recipelist, allergy):
    """
        Iterates through the list and finds recipes with nuts. Used as a key 
        function definition for (sequence unpacking)
        
        Args: filepath (str) - Filepath in which the recipe's are
        
        Returns: A boolean value of whether the indexed recipe has nuts in it, or
        not
    """
    no_allergy=[]
    for r in recipelist:
        recipe,ingredients = [r.name, r.ingredients]
        if allergy not in ingredients:
            no_allergy.append(recipe)
        else:
            continue
    return no_allergy
def get_data1(df):
        """
        Creates a data visual of number of minutes per each dish.
        """
        
        df.hist("Minutes")
        plt.show()
        
        
def get_data2(df):
        """ Creates a data visual representation of the relationship between
        Number of ingredients and the time to cook the overall dish
        """
        sns.lmplot(x = "Ingredients Count", y = "Minutes", data = df)
        plt.show()

    
        
def sorted(df):
    """
        Returns a sorted list of recipes with the fewest to most ingredients.
        (custom key sorting)
        
        Args: filepath (str) - Filepath in which the recipe's are
        
        Returns: A list of recipes with fewest to most ingredients.
    """
    df1 = df.sort_values(["Steps"]).head()
    stepsdf = df1[["Dish", "Ingredients", "Steps"]]
    df2 = df.sort_values(["Minutes"]).head()
    timedf = df2[["Dish", "Ingredients", "Minutes"]]
    print(f"""Dishes that take the fewest steps: 
              
{stepsdf}
              
Dishes that take the shortest amount of time: 

{timedf}""")
          
    
def limited_ingr(ingr_lim=5):
    """Finds recipes with less than 5 ingredients and provides them to user. 
        Args:
            filepath (str): file containing recipes.  
            ingr_lim (int): an integer representing a limited number of ingredients.
                Unless user specifies otherwise the default value is 5. 
                    
        Returns:
            List of recipes with less than 5 ingredients.
    """

    with open("recipes.txt", "r", encoding="utf-8") as f:
        limited_i = []
        for line in f:
            recipe,ingredients = line.split("=")
        if len(ingredients) == ingr_lim:
            limited_i.append(recipe)
        else:
            None
    return limited_i
        
def cuisine(nation, df):
    """
    Filters through given dataframe of foods and returns new dataframe
    containing foods from a user selcted nati on.
        
    Args: 
            nation(str): name of a given nation
            foods(DataFrame): contains all the food opinions
        Returns:
            choice (DataFrame): contains the food opinions from a country 
    """
    nationdf = df[df["Region"] == nation]
    newdf = nationdf[["Dish", "Ingredients"]].reset_index(drop = True)
    return newdf
   
    
def main(filepath):
    recipelist = []
    with open (filepath) as f :
        for line in f:
            split = line.strip().split("=")
            name = split[0]
            ingredients = split[1]
            recipelist.append(Recipe(name, ingredients))
    df = pd.read_csv("Recipes.csv")
    question = input("""Welcome to Cookbook!
                     Choose one of the following options:
                     1. Find a dish based on the ingredients you have at home
                     2. Easy to make recipes
                     3. Cultural dishes
                     4. Cool food data
                     5. Allergy free food
                     """)
    if question == "1":
        user_ing = input("What ingredients do you have?").lower() 
        print(match(recipelist,user_ing)) 
    if question == "2":
        return sorted(df)
        
    if question == "3":
        nation = input("""What region would you like to see? (European, African, South America, North American, East Asian)
                       """)
        print(cuisine(nation, df))
    if question == "4":
        choice = input("""What kind of data do you want to see?
                    1. Distribution of prep time of our various recipes
                    2. Relationship between minutes of prep time and number of ingredients
                    """)
        
        get_data1(df) if choice == "1" else get_data2(df)
        
    if question == "5":
        allergy = input("""What allergy do you have?
                        """).lower()
        print(allergies(recipelist, allergy)) 

    

def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory arguments:
        - filepath (str): path to file containing recipes.

    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", type = str, help="path to recipe and ingredients text file")
    args = parser.parse_args(arglist)
    return args



if __name__ == "__main__":
    filepath = sys.argv[1]
    main(filepath)