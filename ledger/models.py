from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('ledger:ingredient-detail', args=[str(self.pk)])


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    name = models.CharField(max_length=50)
    short_bio = models.TextField(validators=[MinLengthValidator(256)])

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='recipes'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[str(self.pk)])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )

    def __str__(self):
        return f'{self.quantity} of {self.ingredient.name} in {self.recipe.name}'
