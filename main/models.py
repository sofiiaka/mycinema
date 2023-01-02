from django.db import models


class YearProdaction(models.Model):
    year_prodaction = models.CharField('Year prodaction', max_length=4)


class AgeLimit(models.Model):
    age_limit = models.IntegerField('Age limit')


class Country(models.Model):
    country_full_name = models.CharField('Country full name', max_length=100)
    country_short_name = models.CharField('Country short name', max_length=3)


class Genre(models.Model):
    genre = models.CharField('Genre', max_length=50)


class Director(models.Model):
    first_name = models.CharField('First name', max_length=250 )
    last_name = models.CharField('Last name', max_length=250)
    middle_name = models.CharField('Middle name', max_length=250, null=True, blank=True)


class Producer(models.Model):
    first_name = models.CharField('First name', max_length=250)
    last_name = models.CharField('Last name', max_length=250)
    middle_name = models.CharField('Middle name', max_length=250, null=True, blank=True)

class Film(models.Model):
    ukrainian_full_name = models.CharField('Ukrainian full name', max_length=255)
    english_full_name = models.CharField('English full name', max_length=255)
    year_prodaction_id = models.ForeignKey(YearProdaction, on_delete=models.CASCADE)
    age_limit_id = models.ForeignKey(AgeLimit, on_delete=models.CASCADE)
    duration = models.TimeField('Duration')
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    director_id = models.ForeignKey(Director, on_delete=models.CASCADE)
    producer_id = models.ForeignKey(Producer, on_delete=models.CASCADE)