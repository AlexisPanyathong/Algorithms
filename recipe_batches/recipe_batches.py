#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Create an empty list(array)
  potent_batches = []
  
  # Create a for loop of an item in recipe
  for item in recipe:
    # If an item is not in the ingredients return 0(none)
    if item not in ingredients:
        return 0
    # If the item in ingredients is divided by the item in recipes is greater than 0.
    if ingredients[item] // recipe[item] > 0:
      # Append potent_batches with the ingredients[item] // recipe[item], if order to find the amount we need for the recipe.
      potent_batches.append(ingredients[item] // recipe[item])
      
    # Otherwise return 0
    else:
      return 0
 
  # We need to find out how many batches can be made, hence the min.
  return min(potent_batches)     


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))