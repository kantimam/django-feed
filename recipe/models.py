from django.db import models
from django.contrib.postgres.fields import ArrayField


class Ingredient(models.Model):
    name=models.CharField(max_length=128)
    price=models.DecimalField(max_digits=16, decimal_places=2)
    calories_per_unit=models.FloatField()
    calories_per_gram=models.FloatField()

class Recipe(models.Model):
    title=models.CharField(max_length=256)
    calories=models.FloatField()
    description=models.TextField(max_length=2560)
    steps=ArrayField(models.TextField(max_length=256), blank=True)


class RecipeIngredient(models.Model):
    ingredient=models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount_units=models.FloatField(blank=True)
    amount_gram=models.FloatField(blank=True)