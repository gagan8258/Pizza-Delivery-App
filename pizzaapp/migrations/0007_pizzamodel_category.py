# Generated by Django 3.1.6 on 2021-02-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0006_auto_20210129_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzamodel',
            name='category',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
