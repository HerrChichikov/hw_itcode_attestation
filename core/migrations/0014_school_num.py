# Generated by Django 4.2.1 on 2023-07-28 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_home_num_alter_home_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='num',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
