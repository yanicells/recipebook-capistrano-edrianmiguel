from django.urls import path

from . import views

app_name = "ledger"

urlpatterns = [
    path('recipes/list', views.RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/add', views.RecipeCreateView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>/add_image',
         views.RecipeImageCreateView.as_view(), name='recipe-add-image')
]
