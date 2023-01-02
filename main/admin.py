from django.contrib import admin
from .models import Film, Producer, Director, Genre, Country, AgeLimit, YearProdaction

admin.site.register(Film),
admin.site.register(Producer),
admin.site.register(Director),
admin.site.register(Genre),
admin.site.register(Country),
admin.site.register(AgeLimit),
admin.site.register(YearProdaction)
