from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

def index(request):
    # argument name is 'recipe_list'
    return render(request, 'login/index.html')
