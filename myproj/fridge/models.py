
from django.db import models
import datetime
from django.utils import timezone

class User(models.Model):
    user_name = models.CharField(primary_key=True, max_length=200, default='aaa')
    #password
    def __str__(self):
        return self.user_name

class Recipe(models.Model):
    # change user_name to primary key later
    recipe_id = models.IntegerField(primary_key=True, default=0)
    recipe_name = models.CharField(max_length=200)
    recipe_cal = models.IntegerField(default=0)
    recipe_label = models.CharField(max_length=200)
    def __str__(self):
        return self.recipe_name

class Ingredient(models.Model):
    # change user_name to primary key later
    ingredient_id = models.IntegerField(primary_key=True, default=0)
    ingredient_name = models.CharField(max_length=200)
    ingredient_unit = models.CharField(max_length=200)
    ingredient_type = models.CharField(max_length=200)
    def __str__(self):
        return self.ingredient_name

class Recipe_ingredient(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=0)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE, default=0)
    ingredient_quantity = models.IntegerField(default=0)
    class Meta:
        unique_together = (("recipe_id", "ingredient_id"),)

class Recipe_step(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=0)
    step_number = models.IntegerField(default=0)
    step_instructions = models.CharField(max_length=200)
    class Meta:
        unique_together = (("recipe_id", "step_number"),)

class Fridge(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    ingredient_name = models.CharField(max_length=200, default='what') #可自行输入
    quantity = models.IntegerField(default=0)
    #quantity_unit 从ingredient表中找，无法输入，无法用于查找食谱/统计营养
    class Meta:
        unique_together = (("user_name", "ingredient_name"),)


class History(models.Model):
    # change user_name to primary key later
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    ingredient_name = models.CharField(max_length=200) #查找是否有这个ingredient
    ingredient_amount = models.IntegerField(default=0)
    eat_date = models.DateTimeField('date eat')
    def __str__(self):
        return self.user_name