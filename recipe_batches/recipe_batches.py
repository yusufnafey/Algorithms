#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # base case
  batch = 0
  can_make = True

  while can_make:
    for i in recipe:
      # iterate through items in recipe
      if i in ingredients:
        # iterate through ingredients we have
        if recipe[i] <= ingredients[i]:
          # if we have the ingredients, then subtract how much of it we use from the recipe
          ingredients[i] = ingredients[i] - recipe[i]
        else:
          # if we don't, go through iterations again
          can_make = False
      else:
        can_make = False
    if can_make:
      # if we can make one of the recipes, add a batch
      batch += 1
  return batch


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))