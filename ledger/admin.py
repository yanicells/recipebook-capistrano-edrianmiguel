from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
