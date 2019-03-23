from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Recipe, Recipe_ingredient

admin.site.register(Recipe)
admin.site.register(Recipe_ingredient)
