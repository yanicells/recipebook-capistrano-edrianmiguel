from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Ingredient, Profile, Recipe, RecipeImage, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient


class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)
