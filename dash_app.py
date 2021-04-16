import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import re

external_stylesheets = [dbc.themes.UNITED]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Enter Ingredients:"),
    html.Div([dcc.Textarea(id='my-input', value='initial value', cols=100)]),
    html.Br(),
    html.Div(id='my-output'),

])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
#def update_output_div(input_value):
#    return 'Tag Set: {}'.format(input_value)
def generate_tags(ingredient_input, low_fat=False, keto=False):
  ## Process ingredient input ##
  # Remove any parentheses
  ingredient_list_1 = ingredient_input.replace(" (", ", ").replace(")", "")
  # make all lowercase, split to list, remove commas
  ingredient_list = ingredient_list_1.lower().split(", ")

  ## Tag definitions ##
  ingredient_egg = ["egg$"]
  ingredient_beef = ["beef", "steak"]
  ingredient_pork = ["pork", "chorizo"]
  ingredient_chicken = ["chicken"]
  ingredient_seafood = ["shrimp", "salmon",	"cod"]
  paleo_prohib = ['wheat', 'rye', 'parboiled rice', 'barley', 'corn', 'oats',
                  'white potato', 'black bean', 'white rice', 'soy', '^milk',
                  'cheese', 'yogurt', '^butter', 'quinoa', 'brown rice']
  primal_prohib = ['lentil', 'peanut', 'pea', 'corn']
  allergen_dairy = ['^milk', '^butter', 'butterfat', 'cheese', 'lactose',
                    'buttermilk', 'whey', 'casein', 'ghee', 'yogurt']
  whole30_grains = ['wheat', 'rye', 'barley', 'oat', 'corn', 'white rice',
                    'parboiled rice', 'millet', 'bulgur', 'sorghum,',
                    'sprouted grains', 'quinoa', 'amaranth', 'buckwheat',
                    'brown rice', 'red rice']
  whole30_legume = ['bean', 'chickpeas', 'lentil', 'black eyed peas', 'peanut',
                    'soy', 'miso', 'tofu', 'tempeh', 'edamame']
  whole30_sugars = ['sugar', 'syrup', 'allulose', 'dextrose', 'disaccharide',
                    'fructose', 'glucose', 'galactose', 'lactose',
                    'maltodextrin', 'maltose', 'monosaccharide',
                    'polysaccharide', 'ribose', 'saccharose', 'sucrose',
                    'agave nectar', 'coconut nectar', 'coconut sugar',
                    'date sugar', 'cane juice', 'honey', 'maple syrup',
                    'molasses', 'monk fruit extract', 'rice malt', 'sorghum',
                    'treacle', 'coconut crystals']
  whole30_additives = ['carrageenan', 'corn starch', 'monosodium glutamate',
                       'soy lecithin', 'sulfur dioxide', 'sulfite']
  whole30_other = ['dijon mustard']
  whole30_prohib = allergen_dairy+ whole30_grains + whole30_legume + whole30_sugars + whole30_additives + whole30_other
  allergen_egg = ['albumin', 'albumen', 'egg$', 'mayo', 'meringue']
  allergen_shellfish = ['crawfish', 'lobster', 'shrimp', 'crab', 'krill',
                        'prawns']
  allergen_tree_nuts = ['almond', 'beechnut', 'brazil nut', 'cashew',
                        'chestnut', 'coconut', 'filbert', 'hazelnut',
                        'macadamia nut', 'nut butter', 'pecan', 'pine nut',
                        'pinenut', 'pistachio', 'walnut']
  ingredient_onion = ['onion']
  ingredient_garlic = ['garlic']
  ingredient_nightshades = ['ashwagandha', 'tomato', 'cape gooseberries',
                            'capsicum', 'cayenne', 'chili pepper',
                            'chili powder', 'chinese five spice',
                            'chinese 5 spice', 'cocona', 'curry', 'eggplant',
                            'garam masala', 'garden huckleberries',
                            'goji berries', 'kutjera', 'naranjillas',
                            'paprika', 'pepino', 'green pepper', 'red pepper',
                            'yellow pepper', 'bell pepper', 'sweet pepper',
                            'pimento', 'poblano', 'jalapeno', 'potato',
                            'tamarillo', 'tomatillo']
  ingredient_mushrooms = ["mushroom"]
  ingredient_spicy = ['cayenne', 'chili flake', 'chipotle', 'jerk seasoning',
                      'jalapeno', 'blackened seasoning', 'poblano',
                      'crushed red pepper']

  ## Evaluate ingredient list. Search for tagged ingredient in ingredient list. ##
  contains_egg = any(re.search(tag, ingredient) for tag in ingredient_egg
                     for ingredient in ingredient_list)
  contains_beef = any(re.search(tag, ingredient) for tag in ingredient_beef
                      for ingredient in ingredient_list)
  contains_pork = any(re.search(tag, ingredient) for tag in ingredient_pork
                      for ingredient in ingredient_list)
  contains_chicken = any(re.search(tag, ingredient) for tag in ingredient_chicken
                         for ingredient in ingredient_list)
  contains_seafood = any(re.search(tag, ingredient) for tag in ingredient_seafood
                         for ingredient in ingredient_list)
  contains_paleo_prohib = any(re.search(tag, ingredient) for tag in paleo_prohib
                              for ingredient in ingredient_list)
  contains_primal_prohib = any(re.search(tag, ingredient) for tag in primal_prohib
                               for ingredient in ingredient_list)
  contains_whole30_prohib = any(re.search(tag, ingredient) for tag in whole30_prohib
                                for ingredient in ingredient_list)
  contains_dairy = any(re.search(tag, ingredient) for tag in allergen_dairy
                       for ingredient in ingredient_list)
  contains_egg = any(re.search(tag, ingredient) for tag in allergen_egg
                     for ingredient in ingredient_list)
  contains_shellfish = any(re.search(tag, ingredient) for tag in allergen_shellfish
                           for ingredient in ingredient_list)
  contains_tree_nuts = any(re.search(tag, ingredient) for tag in allergen_tree_nuts
                           for ingredient in ingredient_list)
  contains_onion = any(re.search(tag, ingredient) for tag in ingredient_onion
                       for ingredient in ingredient_list)
  contains_garlic = any(re.search(tag, ingredient) for tag in ingredient_garlic
                        for ingredient in ingredient_list)
  contains_nightshades = any(re.search(tag, ingredient) for tag in ingredient_nightshades
                             for ingredient in ingredient_list)
  contains_mushrooms = any(re.search(tag, ingredient) for tag in ingredient_mushrooms
                           for ingredient in ingredient_list)
  contains_spicy = any(re.search(tag, ingredient) for tag in ingredient_spicy
                       for ingredient in ingredient_list)

  ## Create Tag Set ##
  # initialize tag set
  meal_tags = ["diet-gluten-free"]
  # Meal type tags
  if contains_egg == True:
    meal_tags.append("meal-type-breakfast")
  else:
    meal_tags.append("meal-type-lunch-and-dinner")
  # Protein Tags
  if contains_beef == True:
    meal_tags.append("ingredient-beef")
  elif contains_pork == True:
    meal_tags.append("ingredient-pork")
  elif contains_chicken == True:
    meal_tags.append("ingredient-chicken")
  elif contains_seafood == True:
    meal_tags.append("ingredient-seafood")
  else:
    meal_tags.append("ingredient-vegetarian")
  # Diet tags
  if contains_paleo_prohib == False:
    meal_tags.append("diet-paleo")
  if contains_primal_prohib == False:
    meal_tags.append("diet-primal")
  if contains_whole30_prohib == False:
    meal_tags.append("diet-whole-30-approved")
  if low_fat == True:
    meal_tags.append("diet-low-fat")
  if keto == True:
    meal_tags.append("diet-keto")
  # Allergen tags
  if contains_dairy == True:
    meal_tags.append("allergen-dairy")
  if contains_egg == True:
    meal_tags.append("allergen-egg")
  if contains_shellfish == True:
    meal_tags.append("allergen-shellfish")
  if contains_tree_nuts == True:
    meal_tags.append("allergen-tree-nuts")
  if contains_onion == True:
    meal_tags.append("ingredient-onions")
  if contains_garlic == True:
    meal_tags.append("ingredient-garlic")
  if contains_nightshades == True:
    meal_tags.append("ingredient-nightshades")
  if contains_mushrooms == True:
    meal_tags.append("ingredient-mushrooms")
  if contains_spicy == True:
    meal_tags.append("ingredient-spicy")

  # Return final tag set
  return 'Tag Set: {}'.format(meal_tags)
