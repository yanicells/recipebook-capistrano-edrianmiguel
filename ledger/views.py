from django.shortcuts import render
from .models import Ingredient, Recipe, RecipeIngredient

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }

    return render(request, 'ledger/recipe_list.html', ctx)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {
        'recipe': recipe
    }

    return render(request, 'ledger/recipe_detail.html', ctx)