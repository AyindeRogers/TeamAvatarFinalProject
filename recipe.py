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


def introduction(recipelist): 
    
    """Prints out the first and last 10 recipe names in recipelist.
    
    Args: 
        recipelist (list): stores list of recipes 
    
    Returns: 
        
    """

    for r in recipelist: 
        recipe, ingredients = [r.name, r.ingredients]
        return recipe 
    
    RecipeNames = sorted(recipelist, key = introduction)       
         
    print(f"""Here are some of the Recipes you can choose from :
                {RecipeNames}""") 
        
           
def match(recipelist, user_ing): 
    """
    Checks if the user's ingredients satisfy any of the recipes in the 
    textfile by implementing a set intersection. If not, it returns the 
    ingredients the user needs to complete the recipes stored in the
    textfile, through a symmetric difference.
            
    Args: 
        recipeList (list) : stores list of recipes 
        user_ing (set of strings) : contains user's ingredients  
    """
        
    user = user_ing.strip(" ").split(",")
    user_ingredients = set(user)  
    
    for r in recipelist: 
        
        recipe,ingredients = [r.name, r.ingredients] 
        rec_ing = set(r.ingredients)
        match = user_ingredients & rec_ing
        
        if match and len(match) == len(rec_ing):
                    print(f"You can make {r.name}")
            
        else :  
            print(f"""None of your ingredients match our recipes.""")
               
    
    
def allergies(recipelist, allergy):
    """ 
        Ayinde - (Sequence Unpacking)
        Iterates through the list and finds recipes with nuts. Used as a key 
        function definition for (sequence unpacking)
        
        Args: filepath (str) - Filepath in which the recipe's are
              allergy (str) - Allergy User input passed in from the main 
              function.
        
        Returns: A list of recipes that do not have the allergy ingredient
        in them.
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
        Ayinde - Data Visualization
        Creates a data visual of number of minutes per each dish.
        
        Args:
            df - dataframe of the csv that we are working in
            
        Returns:
            a graphical display of informaton
        """
        
        df.hist("Minutes")
        plt.show()
        
        
def get_data2(df):
        """ 
        Ayinde - Data Visualization
        Creates a data visual representation of the relationship between
        Number of ingredients and the time to cook the overall dish
        Args:
            df - dataframe of the csv that we are working in
            
        Returns:
            a graphical display of informaton
        """
        sns.lmplot(x = "Ingredients Count", y = "Minutes", data = df)
        plt.show()

    
        
def sorted(df):
    """
    Creates two DataFrames: one sorted based on the number of steps in a
    recipe and another on the amount of time it takes to make a food.
    Returns the top 5 foods in both DataFrames. 

    Args:
        df(DataFrame): contains recipe information

    Returns:
        Five dishes that take the fewest number of steps and five dishes that
        take the shortest amount of time. 
    """
    
    df1 = df.sort_values(["Steps"]).head()
    stepsdf = df1[["Dish", "Ingredients", "Steps"]]
    df2 = df.sort_values(["Minutes"]).head()
    timedf = df2[["Dish", "Ingredients", "Minutes"]]
    return(f"""Dishes that take the fewest steps: 
              
{stepsdf}
              
Dishes that take the shortest amount of time: 

{timedf}""")
          
    
def limited_ingr(filepath, ingr_lim=5):
    """Finds recipes with 5 or specific number of ingredients and provides them to user. 
    Args:
        filepath (str): text file containing recipes.  
        ingr_lim (int): an integer representing a limited number of ingredients.
            Unless user specifies otherwise the default value is 5. 
                 
    Returns:
        List of recipes with 5 or specified number of ingredients.
    """
    limited_i = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            recipe,ingredients = line.split("=")
            ilist = ingredients.split(",")
            #print(ilist)
            if len(ilist) == ingr_lim:
                limited_i.append(recipe)
                
    return limited_i
        
def cuisine(region, df):
    """
    Filters through dataframe of foods and returns new dataframe
    containing foods from a user selcted nation.

    Args:
        region(str): name of a given region
        df(DataFrame): contains recipe information

    Returns:
        newdf(DataFrame): only contains foods from a selected region
    """
    regiondf = df[df["Region"] == region]
    newdf = regiondf[["Dish", "Ingredients"]].reset_index(drop = True)
    return newdf

      
def main(filepath):
    """
    Opens textfile and DataFrame into program. Asks user which
    program functionality they want to see and prints calls function
    associated with their choice. 

    Args:
        filepath(str): path to textfile containing recipe information

    Side effects:
        Display message to user based on user input.
    """
    
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
                     6. Take a look at our recipes
                     """)
    if question == "1":
        user_ing = input("What ingredients do you have?").lower() 
        print(match(recipelist,user_ing)) 
            
    if question == "2":
        print(sorted(df))
        print(f"Dishes with 5 or fewer ingredients:{limited_ingr(f)}")
        
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
        
    if question == "6": 
        print(introduction(recipelist))

    

def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory arguments:
        - filepath (str): path to file containing recipes.

    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as namespace, value is path to text 
            file.
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", type = str, help="path to recipe and ingredients text file")
    args = parser.parse_args(arglist)
    return args



if __name__ == "__main__":
    filepath = sys.argv[1]
    main(filepath)