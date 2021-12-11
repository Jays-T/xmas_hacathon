from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import AdminRecipeForm


@login_required
def show_recipes(request):
    
    recipes = Recipe.objects.all()

    template = 'recipes/show_recipes.html'
    context = {
        "recipes": recipes,
    }

    return render(request, template, context)
