from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import AdminRecipeForm
import random
from random import sample


@login_required
def show_recipes(request):
    """ Placeholder proof of concept for recipes """
    recipes = Recipe.objects.all()

    random_selection = random.sample(list(recipes), 1)
    print(f'recipes are: {random_selection}')

    template = 'recipes/show_recipes.html'
    context = {
        "recipes": recipes,
    }

    return render(request, template, context)
