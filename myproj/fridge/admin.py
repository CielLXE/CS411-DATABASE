from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Recipe, Recipe_ingredient, User, Fridge, Recipe_step,Ingredient

admin.site.register(Recipe)
admin.site.register(Recipe_ingredient)
admin.site.register(User)
admin.site.register(Fridge)
admin.site.register(Recipe_step)
admin.site.register(Ingredient)
