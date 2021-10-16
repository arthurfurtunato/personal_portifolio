from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    blog = Blog.objects.order_by('-date_post')[:3]
    return render(request, 'blog/index.html', {
        'blog': blog,
    })