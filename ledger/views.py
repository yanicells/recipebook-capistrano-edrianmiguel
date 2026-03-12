from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import RecipeForm, RecipeImageFrom
from .models import Recipe, RecipeImage


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    context_object_name = 'recipe'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'ledger/recipe_form.html'

    def get_success_url(self):
        return reverse_lazy('ledger:recipe-detail', kwargs={'pk': self.object.pk})


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageFrom
    template_name = 'ledger/recipeimage_form.html'

    def form_valid(self, form):
        recipe_image = form.save(commit=False)
        recipe_image.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        recipe_image.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('ledger:recipe-detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_pk'] = self.kwargs['pk']
        return context
