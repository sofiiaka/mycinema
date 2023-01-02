# Generated by Django 4.1.4 on 2022-12-30 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeLimit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_limit', models.IntegerField(verbose_name='Age limit')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_full_name', models.CharField(max_length=100, verbose_name='Country full name')),
                ('country_short_name', models.CharField(max_length=3, verbose_name='Country short name')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, verbose_name='First name')),
                ('last_name', models.CharField(max_length=250, verbose_name='Last name')),
                ('middle_name', models.CharField(max_length=250, verbose_name='Middle name')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50, verbose_name='Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, verbose_name='First name')),
                ('last_name', models.CharField(max_length=250, verbose_name='Last name')),
                ('middle_name', models.CharField(max_length=250, verbose_name='Middle name')),
            ],
        ),
        migrations.CreateModel(
            name='YearProdaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_prodaction', models.DateField(verbose_name='Year prodaction')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ukrainian_full_name', models.CharField(max_length=255, verbose_name='Ukrainian full name')),
                ('english_full_name', models.CharField(max_length=255, verbose_name='English full name')),
                ('duration', models.TimeField(verbose_name='Duration')),
                ('age_limit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.agelimit')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.country')),
                ('director_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.director')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.genre')),
                ('producer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producer')),
                ('year_prodaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.yearprodaction')),
            ],
        ),
    ]
