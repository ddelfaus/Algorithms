#!/usr/bin/python
# this function should compare each dictionary to check if on how many batches you can make with the givin recipes
#check if recipe and ingredients match
#check how many batches you can make
import math
def recipe_batches(recipe, ingredients):
  max_batches = 0

  recipe_keys = set(recipe.keys())
  ingredients_keys = set(ingredients.keys())


  common_ingredients = set(recipe_keys).intersection(set(ingredients_keys))

  if len(common_ingredients) != len(recipe):
    return 0
  for key, value in ingredients.items():
    
    batch = value // recipe[key]

    if max_batches is 0 or batch < max_batches:
      max_batches = batch
  return max_batches
  
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))