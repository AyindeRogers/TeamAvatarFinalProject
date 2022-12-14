import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys
from argparse import ArgumentParser


class Recipe: 
    """Creates Recipe objects that display dish name and ingredients. 
    
    Attributes: 
    
        name (str): dish name
        ingredients (str): dish ingredients 
    """
    def __init__(self, name, ingredients):
        """Instantiates Recipe attributes. 
        
        Args: 
            name (str): dish name 
            ingredients (str): dish ingredients 
            
        Side effects: 
            Sets attributes 'name', 'ingredients'. 
        """
        self.name = name
        self.ingredients = ingredients.split(",")
    
    def __str__(self):
        """Caleb - magic methods
        Returns informal representation of Recipe objects."""
        
        return f"{self.ingredients}"


def ChooseLetter(recipelist, letter): 
    
    """Brooke - keyword arguments 
    Returns list of recipes that starts with a letter chosen by user passed 
    as a key argument in the main function. 
    
    Args: 
        recipelist (list): stores list of recipes 
        letter (str): letter entered by user
    
    Returns: 
        RecipeLetter (list): recipes that start with letter chosen by user.
    """
    RecipeLetter = [] 
    
    for r in recipelist: 
        if r.name.startswith(letter): 
            RecipeLetter.append(r.name)

    return RecipeLetter
                
                
def match(recipelist, user_ing): 
    """Brooke - set operations
    Checks if the user's ingredients satisfy any of the recipes in the 
    textfile by implementing a set intersection and difference. 
            
    Args: 
        recipelist (list) : stores list of recipes 
        user_ing (str) : contains user's ingredients  
        
    Returns: 
         Either a dish name (str) that the user can make or a
         set of ingredients user still needs (if they have 2 or more of the 
         necessary ingredients) to complete a dish.
    """
        
    user = user_ing.strip().split(",")
    user_ingredients = set(user)  
    
    for r in recipelist: 
        
        rec_ing = set(r.ingredients)
        match = user_ingredients & rec_ing
    
         
        if match:
            if len(match) == len(rec_ing):
                return (f"""You can make {r.name}!
                       """)
            else:
                if len(match) > 1: 
                    return(f"""To make {r.name} you still need:
{rec_ing - user_ingredients}
    """)
    
               
    
def allergies(recipelist, allergy):
    """Ayinde - Sequence Unpacking
        Iterates through the list and finds recipes with nuts. Used as a key 
        function definition for (sequence unpacking)
        
        Args: 
            filepath (str) - Filepath in which the recipe's are
            allergy (str) - Allergy User input passed in from the main 
            function.
        
        Returns: 
            no_allergy (list) - A list of recipes that do not have the allergy 
            ingredient in them.
    """
    no_allergy=[]
    for r in recipelist:
        recipe,ingredients = [r.name, r.ingredients]
        if allergy not in ingredients:
            no_allergy.append(recipe)
        else:
            continue
    return (f"""Here are foods that don't contain {allergy}:
            
{no_allergy}""""")


def get_data1(df):
        """Ayinde - Data Visualization
        Creates a data visual of number of minutes per each dish.
        
        Args:
            df - dataframe of the csv that we are working in
            
        Returns:
            a graphical display of informaton
        """
        
        df.hist("Minutes")
        plt.title("Distribution of Minutes across the Dishes")
        plt.xlabel("Minutes")
        plt.ylabel("# of Dishes")
        plt.show()
        
        
def get_data2(df):
        """Ayinde - Data Visualization
        Creates a data visual representation of the relationship between
        Number of ingredients and the time to cook the overall dish
        Args:
            df - dataframe of the csv that we are working in
            
        Returns:
            a graphical display of informaton
        """
        sns.lmplot(x = "Ingredients Count", y = "Minutes", data = df)
        plt.title('Distribution of Ingredient Count and Minutes')
        plt.show()

    
        
def sorted(df):
    """Semhar - Pandas
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
          
    
def limited_ingr(recipelist):
    """Bella - List Comprehension
    Finds recipes with five or less ingredients and provides them to user. 
    
    Args:
        recipelist (list): stores list of recipes.
                    
    Returns:
        F-string containing list of recipes with 5 or less of ingredients.
    """
    for line in recipelist:
        
        recipe, ingredients = [line.name, line.ingredients]
        
        five_ing = [(i.name) for i in recipelist if len(i.ingredients) <= 5]
        
    return f"""
The following dishes require 5 ingredients or less to prepare: 

{five_ing}"""
        
        
def cuisine(region, df):
    """Semhar - Pandas
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


def get_ingredients(dishName, recipeLst):
    """ Caleb - f-strings
    Purpose- The funciton uses a for loop to go through recipes in the recipeLst
    and has a if statement that looks to see if the dish name is in the recipe Name.
    
    Args:
    dishName(str): string of the dish name
    recipeLst(lst): list of the recipies with ingredients
    
    Return:
    if the name is found in the list a f string will appear with Here are its 
    ingredients with the ingredients following it.
    """
    for recipe in recipeLst:
        if dishName == recipe.name:
            return f"Here are its ingredients: {recipe.ingredients}"


def main(filepath):
    """Semhar - conditional expressions, with statement
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
    question = ""
    while question != "7":
        
        question = input("""
                    Welcome to Cookbook!
                    Choose one of the following options:
                     1. Table of Contents
                     2. Find a Dish Based on the Ingredients You Have at Home
                     3. Easy to Make Recipes
                     4. Cuisines
                     5. Food Data
                     6. Allergy Free Food
                     7. Quit
                     """)
        if question == "1": 
            starts = input("""Enter the letter the dish starts with.
                           """)
            if ChooseLetter(recipelist, letter = starts.upper()) != []:
                print(ChooseLetter(recipelist, letter = starts.upper()))
                dish = input("""
Select a dish by typing it out exactly as it appears above.
                         """)
                print(get_ingredients(dish, recipelist))
            else:
                print(f"""Sorry, we don't have any foods that start with 
                      {starts.upper()} in our cookbook.""")
            
        if question == "2":
            user_ing = input("""What ingredients do you have? (ex. milk,cheese)
                             """).lower() 
            print(match(recipelist,user_ing) if match(recipelist,user_ing)!= None
                  else f"""
Sorry, you don't have enough ingredients to make one of our dishes.""")
           
            
        if question == "3":
            print(sorted(df))
            
            print(limited_ingr(recipelist))
        
        if question == "4":
            nation = input("""What region would you like to see? 
            (European, African, South America, North American, East Asian)
            """)
            print(cuisine(nation, df))
        if question == "5":
            choice = input("""What kind of data do you want to see?
                    1. Distribution of prep time of our various recipes
                    2. Relationship between minutes of prep time and number of 
                    ingredients
                    """)
            if choice == "1":
                get_data1(df) 
            elif choice == "2": 
                get_data2(df)
        
        if question == "6":
            allergy = input("""What allergy do you have?
                        """).lower()
            print(allergies(recipelist, allergy)) 
        

def parse_args(arglist):
    """ Bella - Argument Parser Class 
    Parse command-line arguments.
    
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
