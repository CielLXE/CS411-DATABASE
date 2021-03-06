# Generated by Django 2.1.7 on 2019-03-23 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fridge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('recipe_name', models.CharField(max_length=200)),
                ('recipe_ins', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe_ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('quantity_unit', models.CharField(max_length=200)),
                ('recipe_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='fridge.Recipe')),
            ],
        ),
        migrations.RemoveField(
            model_name='fridge',
            name='user_name',
        ),
        migrations.DeleteModel(
            name='Fridge',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
