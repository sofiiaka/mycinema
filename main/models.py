from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Country(models.Model):
    country_full_name = models.CharField('Country full name', max_length=100)
    country_short_name = models.CharField('Country short name', max_length=3)


class Genre(models.Model):
    genre = models.CharField('Genre', max_length=50)


class Film(models.Model):
    title = models.CharField('Title', max_length=255)
    year_production = models.CharField('Year production id', max_length=10, default=timezone.now)
    overview = models.CharField('Overview', max_length=2500)
    duration = models.CharField('Duration', max_length=4)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    remark = models.TextField('Remark', null=True)
    own_rating = models.IntegerField('Own rating', validators=[MaxValueValidator(10), MinValueValidator(1)], null=True)