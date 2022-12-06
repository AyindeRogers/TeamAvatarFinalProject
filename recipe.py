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
    def __repr__():
        """Produce a formal list representation of the object ingredients.

    Args:
    The formal representation will have the form “**Food**insert our ingredients**”
    Where ing1, ing2, ing3, ing4…..  are the components of this food.

    This representation is suitable for debugging and can be used as code
        to recreate this object.

    Returns:
    Lst: the list representation
    """
        return
    
def match(recipeList, user_ing): 
    """
    Checks if the user's ingredients satisfy any of the recipes in the 
    textfile by implementing a set intersection. If not, it returns the 
    ingredients the user needs to complete 5 recipes stored in the
    textfile, through a symmetric difference.
            
    Args: 
        recipeList (str) : stores list of recipes 
        user (set of strings) : contains ingredients user has 
                
    Returns: 
        Match (set of strings): Recipe(s) a user has the correct 
        ingredients for 
        (set of strings): Ingredients a user needs to 
        complete 5 recipes stored in the filepath. 
    """
        
    user = user_ing.split(",")
    user_ingredients = set(user)  
    
    for r in recipeList:
        recipe,ingredients = [r.name, r.ingredients] 
        match = user_ingredients & set(r.ingredients)
        if match and len(match) == len(user_ingredients):
            print(f"You can make {r.name}")
        
        else:
            counter = 0 
            while counter == 5:
                for line in recipeList: 
                    print(f"""In order to make {r.name} = 
                        {set(r.ingredients) - user_ingredients}""")
                    counter -= 1 
    
    
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

def read_function(filepath):
    """ 
        Uses a with statement to open a file then a read function for a text file 
    that has the food with ingredients along with a pandas file.

    Args:
        Text file of the foods followed by a list of ingredients along with a pandas 
    file that has the name of the dish, country of cuisine, and number of 
    instructions for the column names.

    Returns:
        Str: 
    returns the specified data that was previously written in the specified text 
    file and the pandas file provided. 

        """
    
        
def sorted_steps(df):
    """
        Returns a sorted list of recipes with the fewest to most ingredients.
        (custom key sorting)
        
        Args: filepath (str) - Filepath in which the recipe's are
        
        Returns: A list of recipes with fewest to most ingredients.
    """
    df1 = df.sort_values(["Steps"]).head()
    stepsdf = df1[["Dish", "Ingredients", "Steps"]]
    return(stepsdf)

def sorted_time(df):
    """
        Returns a sorted list of recipes with the fewest to most ingredients.
        (custom key sorting)
        
        Args: filepath (str) - Filepath in which the recipe's are
        
        Returns: A list of recipes with fewest to most ingredients.
    """
    df2 = df.sort_values(["Minutes "]).head()
    timedf = df2[["Dish", "Ingredients", "Minutes "]]
    return(timedf)
          
    
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
    user_ing = input("What ingredients do you have?").lower()
    print(match(recipelist,user_ing)) 
    # nation = input("""Pick your desired region : South America, Africa,
    #                     Middle East, Europe, Asia""")  
    # print("Your region is" + nation)

    #foods = input("What ingredients do you have?")
    #foods = "quinoa,water"
    #nation = "South America"
    #(f"You have {foods}")

    #print(cuisine(nation, foods))
    get_data1(df)
    get_data2(df)
    
    allergy = input("Do you have any allergies?").lower()
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
    
    return parser.parse_args(arglist)


if __name__ == "__main__":
    main("recipes.txt")