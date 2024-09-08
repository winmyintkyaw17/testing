from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name = 'home'),
    path('about_us', views.about, name= 'about'),
    path('blog/<int:id>',views.article, name ='post'),
    path('blog/name/<str:name>',views.articlebyname, name ='postname'),
    path('blog/search', views.search_article, name ='search_article'),
    path('blog/add', views.add_post, name='add_post'),
    path('blog/add/db', views.add_post_to_database, name='add_post_to_database')
]