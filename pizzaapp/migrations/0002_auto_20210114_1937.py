# Generated by Django 3.1.2 on 2021-01-14 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizzamodel',
            old_name='pizza',
            new_name='name',
        ),
    ]
