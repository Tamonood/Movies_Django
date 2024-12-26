# view is a function

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

def movies(request):
    data = Movie.objects.all() # to retrieve data from database
    return render(request, 'movies/movies.html', {'movies': data})  # rearranging template - 'movies/movies.html'
'''

Mock data
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
'''
    
    #return render(request, 'movies/movies.html',data)
def home(request):
    return HttpResponse("Welcome to the Movies Homepage!")

def homealone(request):
    return HttpResponse("Homealone")

def detail(request, id):
    data = Movie.objects.get(pk=id) # ask certain primary key based on variable id
    return render(request, 'movies/detail.html', {'movie': data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')
    
    return render(request, 'movies/add.html')
    
def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')
    movie.delete()
    return HttpResponseRedirect('/movies')