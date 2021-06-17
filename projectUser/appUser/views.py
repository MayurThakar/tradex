from django.shortcuts import render
from appUser.main import Main

# Create your views here.


def index(request):
    if request.method == 'POST':
        reference = Main(request)

        if (error := reference.is_exist()) == True:
            posts = reference.fetch()
            return render(request, 'homepage.html', {
                'posts': posts,
                'user_name': request.POST['user-name']})

        else:
            return render(request, 'index.html', {
                'has_error': error,
                'user_name': request.POST['user-name'],
                'password': request.POST['password']})

    return render(request, 'index.html')


def homepage(request):
    if request.method == 'POST' and 'post-button' in request.POST:
        reference = Main(request)
        reference.create_post()
        posts = reference.fetch()
        return render(request, 'homepage.html', {
            'posts': posts,
            'user_name': request.POST['post-button']})

    return render(request, 'homepage.html')
