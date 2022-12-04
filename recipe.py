import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys
from argparse import ArgumentParser


if __name__ == "__main__":
    try: 
        args = parse_args(sys.argv[1:])
    except ValueError as a:
        sys.exit(str(a))
        
def allergy(recipelist, allergy):
    """
        Iterates through the list and finds recipes with nuts. Used as a key 
        function definition for (sequence unpacking)
        
        Args: filepath (str) - Filepath in which the recipe's are
        
        Returns: A boolean value of whether the indexed recipe has nuts in it, or
        not
    """
    #no_allergy=[]
    #for r in recipelist:
        #recipe,ingredients = [r.recipe, r.ingredients]
        #if allergy not in ingredients:
            #no_allergy.append(recipe)
        #else:
            #continue
    #return no_allergy

class Recipe: 
    def __init__(self, recipe, ingredients):
        self.recipe = recipe
        self.ingredients = ingredients
    
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
    def match(filepath, ingredients): 
        """
        Checks if the user's ingredients satisfy any of the recipes in the 
        textfile by implementing a set intersection. If not, it returns the 
        ingredients the user needs to complete all of the recipes stored in the
        textfile, through a symmetric difference.
        
        Args: 
            filepath (str) : stores set of recipes 
            ingredients (set of strings) : contains ingredients user has 
            
        Returns: 
            Match (set of strings): Recipe(s) a user has the correct ingredients for 
            Incomplete (set of strings): Ingredients a user needs to complete all 
            of the recipes stored in the filepath. 
        """
        
    def sorted_recipes(filepath):
        """
        Returns a sorted list of recipes with the fewest to most ingredients.
        (custom key sorting)
        
        Args: filepath (str) - Filepath in which the recipe's are
        
        Returns: A list of recipes with fewest to most ingredients.
        """
        
    def get_data(filepath):
        """
        Creates a data visual of most difficult recipes to make by Region,
        and the longest recipes to make by region
        """
        #df = pd.read_csv("Recipes.csv")
        #To show what regions have the most complicated dishes
        #df.plot.bar(x = "Region", y = "Steps")
        #plt.show()
        #To show the distrubution of minutes
        #df.hist("Minutes")
        #plt.show()
        #To show if there is any relationship between Ingredients and Cook time
        #sns.lmplot(x = "Ingredients Count", y = "Minutes", data = df)
        #plt.show()
        

    def limited_ingr(filepath):
        """Finds recipes with less than 5 ingredients and provides them to user. 
        Args:
            filepath (str): file containing recipes.  
                    
        Returns:
            List of recipes with less than 5 ingredients.
        """
    
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
    
    def cuisine(nation, foods):
        """
        Filters through given dataframe of foods and returns new dataframe
        containing foods from a user selcted nati on.
        
        Args: 
            nation(str): name of a given nation
            foods(DataFrame): contains all the food opinions
        Returns:
            choice (DataFrame): contains the food opinions from a country 
        """
        return

def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory arguments:
        - filepath (str): path to file containing recipes.
        - allergy (str): food allergen.
        - ingredients (set of strings): set of strings of ingredients.
    
    Expect the following optional arguments:
        -c, --ingr_lim: if specified, include recipes with limited number of ingredients.
        -v, --nation: if specified, it should be cuisine/the nation the recipe comes from.
        
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to recipe and ingredients text file")
    parser.add_argument("allergy", help="allergens")
    parser.add_argument("ingredients", help="ingredients set of strings")

    parser.add_argument("-c", "--ingr_lim", action="store_true",
                        help="add an ingredient limit")
    parser.add_argument("-v", "--nation", help="region cuisine is from")
    return parser.parse_args(arglist)
    
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
    parser.add_argument("filepath", help="path to recipe and ingredients text file")
    
    return parser.parse_args(arglist)