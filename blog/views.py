from django.shortcuts import render, get_object_or_404
from .models import Posts



# Create your views here.
def blog(request):
    posts = Posts.objects.all()
    return render(request, 'blog.html', {'posts':posts}, )


def all_blogs(request):
    posts = Posts.objects.all()
    return render(request, 'blog/all_blogs.html', {'posts':posts})

def blog_page(request, blog_id):
#    posts = Posts.objects.filter(pk=blog_id)
    post = get_object_or_404(Posts,pk=blog_id)
# {'posts':posts}, {'post':post}
    return render(request, 'blog/blog_page.html', {'post':post}, {'id':blog_id} )




'''
7*8
10*8
1-этаж
общепит на вынос
Партенит
потолок - веранда
'''
