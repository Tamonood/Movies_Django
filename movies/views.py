# view is a function

from django.http import HttpResponse
from django.shortcuts import render
#from .models import Movie

def movies(request):
    # data = Movie.objects.all()

    data = {
        'movies': [
            {
                'id': 5,
                'title': 'Jaws',
                'year': 1969
            },
            {
                'id': 2,
                'title': 'Sholay',
                'year': 1960
            },
            {
                'id': 4,
                'title': 'Jaws2',
                'year': 1989
            },
        ]
    }

    #return render(request, 'movies/movies.html', {'movies': data})  # araanging template - 'movies/movies.html'
    return render(request, 'movies/movies.html',data)
def home(request):
    return HttpResponse("Welcome to the Movies Homepage!")

def homealone(request):
    return HttpResponse("Homealone")