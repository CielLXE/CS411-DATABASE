
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Recipe, Recipe_ingredient

def index(request):
    recipe_list = Recipe.objects.all()
    context = {'recipe_list': recipe_list}
    #argument name is 'recipe_list'
    return render(request, 'fridge/index.html', context)

def detail(request, r_id):
    recipe = get_object_or_404(Recipe, recipe_id=r_id)
    ingredient_list = Recipe_ingredient.objects.filter(recipe_id=r_id)
    context = {'recipe':recipe, 'ingredient_list':ingredient_list }
    return render(request, 'fridge/detail.html', context)