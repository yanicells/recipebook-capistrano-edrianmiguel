from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_self_url(self):
        return reverse('ledger:ingredient-detail', args=[str(self.pk)])
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_self_url(self):
        return reverse('ledger:recipe-detail', args=[str(self.pk)])
    
class RecipeIngredient(models.Model):
    quantity = models.FloatField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return '{} {} of {}'.format(self.quantity, self.ingredient.name, self.recipe.name)