# Generated by Django 4.1.4 on 2023-01-10 23:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_year_prodaction_id_film_year_prodaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='year_prodaction',
        ),
        migrations.AddField(
            model_name='film',
            name='year_production',
            field=models.CharField(default=django.utils.timezone.now, max_length=10, verbose_name='Year production id'),
        ),
    ]
