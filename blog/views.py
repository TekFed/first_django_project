from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'tekfed',
        'title': 'Core Computing',
        'content': 'Hello World!',
        'date_posted': 'October 14, 2002'
    },
    {
        'author': 'Mary',
        'title': 'Juliet Has Arrived!',
        'content': 'The one and only',
        'date_posted': 'December 20, 2024'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
