from django.shortcuts import render, get_object_or_404
import blog
from .models import Blog

# Create your views here.
def index(request):
    blog = Blog.objects.order_by('-date_post')[:5]
    return render(request, 'blog/index.html', {
        'blog': blog,
    })

def detail(request, blog_id):
    blog = Blog.objects.filter(id=blog_id).first
    return render(request, 'blog/detail.html', {
        'blog': blog
    })