# Generated by Django 4.1.4 on 2023-01-18 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_film_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='country_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.country'),
        ),
    ]