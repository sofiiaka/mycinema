# Generated by Django 4.1.4 on 2023-01-09 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_film_year_prodaction_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='YearProdaction',
        ),
    ]
