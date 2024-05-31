from django.shortcuts import render,redirect
from .forms import *asd
from .models import *
from .search_index import *
from elasticsearch_dsl import Search


from .search_index import PostDocument
from datetime import datetime
def Home(request):
    if request.method == 'POST':
        search_query = request.POST.get('q')
        search = Search(index='posts').filter('multi_match', query=search_query, fields=['content', 'author'])
        results = search.execute()
        return render(request, 'search.html', {'results': results, 'search_query': search_query})
    else:
        posts = Posts.objects.all() 
        return render(request, 'index.html', {'Posts': posts})
 
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # После успешной регистрации перенаправляем на страницу входа
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def create_post(request):
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostsForm()
    return render(request, 'post_create.html', {'form': form})
