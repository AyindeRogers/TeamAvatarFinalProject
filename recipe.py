
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
def find_nuts(filepath):
    """
    Iterates through the list and finds recipes with nuts. Used as a key 
    function definition for no_nut_recipes function
    
    Args: filepath (str) - Filepath in which the recipe's are
    
    Returns: A boolean value of whether the indexed recipe has nuts in it, or
    not
    """
def no_nut_recipe(filepath):
    """ Returns a list of recipe's with no nuts in them
    
        Args: filepath (str) - Filepath in which the recipe's are
        
        Returns: A list of Recipe's with no nuts in the recipe.
    """
    
def get_recipe(ingredients):
    """
    Checks the given ingredients by user against stored recipes to either 
    return matching recipe or missing ingredients.
    
    Args:
        ingredients (str): the ingredients the user has
    
    Returns:
        result (str): a food name or missing ingredients 
    """
    return

def limited_ingr(filepath):
    """Finds recipes with less than 5 ingredients and provides them to user. 
    Args:
        filepath (str): file containing recipes.  
                 
    Returns:
        List of recipes with less than 5 ingredients.
    """
    
def cuisine(nation, foods):
    """
    Filters through given dataframe of foods and returns new dataframe
    containing foods from a user selcted nation.
    
    Args: 
        nation(str): name of a given nation
        foods(DataFrame): contains all 
    Returns:
        choice (DataFrame): contains the food opinions from a country 
    """
    return

def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory arguments:
        - filepath (str): path to file containing recipes. 
    
    Expect the following optional arguments:    
        - 
        
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as namespace.
    """