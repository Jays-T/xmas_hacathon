from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import AdminRecipeForm
import random
from random import sample


@login_required
def show_recipe(request, recipe_id):
    """ Placeholder proof of concept for recipes """
    recipe = get_object_or_404(Recipe, id=recipe_id)

    template = 'recipes/show_recipe.html'
    context = {
        "recipe": recipe,
    }
    messages.success(request, 'A most excellent choice!')
    messages.warning(request, 'This is making me even more hangry!')

    return render(request, template, context)
