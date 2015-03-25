from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from skatehuntapp.forms import NewUserCreationForm, PostForm


# Single Page
from skatehuntapp.models import Post


def home(request):
    posts = Post.objects.all()
    data = {'posts':posts}

    return render(request, "index.html", data)


# View to create a new account
def register(request):
    if request.method == 'POST':
        form = NewUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.image = request.FILES['image']
            form.save()
            return redirect('home')
    else:
        form = NewUserCreationForm()

    return render(request, 'registration/register.html', {
        'form': form,
    })


# View to submit a new post
@login_required
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print 'post req received'
        print form
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            Post.objects.create(
                user=user,
                title=title,
                description=description,
            )
            return HttpResponse(status=200)
        else:
            print 'invalid form'
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)