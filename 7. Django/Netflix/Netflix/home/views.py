from django.shortcuts import render

# Create your views here.
def movie(request):
    context = {
        'movie_name' : 'Inception',
        'genre' : 'Sci-Fi'
    }
    return render(request, 'movie.html', context)