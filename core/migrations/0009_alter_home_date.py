# Generated by Django 4.2.1 on 2023-07-20 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_home_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='date',
            field=models.DateField(),
        ),
    ]