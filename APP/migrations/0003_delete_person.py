# Generated by Django 4.2.2 on 2023-07-08 06:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("APP", "0002_alter_person_personal_details"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Person",
        ),
    ]