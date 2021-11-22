from django.shortcuts import get_object_or_404, render
from .models import Category, Post

def blog(request):
    _all_posts = Post.objects.all()
    context={'title':'Blog', 'posts':_all_posts}
    return render(request, 'blog/blog.html', context=context)

def category(request, category_id ):
    category = get_object_or_404(Category, id=category_id )
    _all_posts = category.get_posts.all()
    context={'title':category.name, 'posts':_all_posts}
    return render(request, 'blog/blog.html', context=context)
