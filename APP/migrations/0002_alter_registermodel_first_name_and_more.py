# Generated by Django 4.2.2 on 2023-07-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("APP", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registermodel",
            name="first_name",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="registermodel",
            name="last_name",
            field=models.TextField(),
        ),
    ]
