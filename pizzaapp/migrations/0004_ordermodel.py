# Generated by Django 3.1.2 on 2021-01-28 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0003_customermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('phoneno', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=10)),
                ('ordereditems', models.CharField(max_length=10)),
            ],
        ),
    ]
