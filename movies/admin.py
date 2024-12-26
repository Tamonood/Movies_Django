# to show the tables in admin page
from .models import Movie

from django.contrib import admin # to get refernce to admin page

admin.site.register(Movie)