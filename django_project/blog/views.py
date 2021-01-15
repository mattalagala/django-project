from django.shortcuts import render

posts = [{
    'author': 'MattA',
    'title': 'Blog Post 10',
    'content': 'First post content',
    'date_posted': 'August 27, 2018'
},
{
    'author': 'MattA2',
    'title': 'ds',
    'content': 'First post content22',
    'date_posted': 'August 27, 20182'
} ]

def home (request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about (request):
    return render(request, 'blog/about.html')