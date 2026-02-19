from django.urls import path
from .views import recipe_detail, recipe_list

app_name = "ledger"

urlpatterns = [
    path('recipes/list', recipe_list, name='recipe-list'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe-detail'),
]