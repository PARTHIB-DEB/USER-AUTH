# Generated by Django 4.2.2 on 2023-07-09 16:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("APP", "0002_alter_registermodel_first_name_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="RegisterModel",
        ),
    ]
