# Generated by Django 4.1.7 on 2023-05-09 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0004_restaurant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="food_remains_available",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="fresh_food_available",
            field=models.CharField(max_length=100),
        ),
    ]
