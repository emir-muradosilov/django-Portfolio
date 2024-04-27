
from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
#    path('', views.tree, name = 'blog/'),
#    path('tree/', views.tree, name = 'blog'),
#    path('<int:id>/', ArticleDetailView.as_view(), name = 'blog_page'),
    path('<int:blog_id>/', views.blog_page, name = 'blog_page'),
]
