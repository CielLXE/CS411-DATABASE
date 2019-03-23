
from django.db import models


class Recipe(models.Model):
    # change user_name to primary key later
    recipe_id = models.IntegerField(primary_key=True,default=0)
    recipe_name = models.CharField(max_length=200)
    recipe_ins = models.CharField(max_length=200)
    def __str__(self):
        return self.recipe_name

class Recipe_ingredient(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE,default = 0)
    ingredient_name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    quantity_unit = models.CharField(max_length=200)

    def __str__(self):
        return self.ingredient_name

