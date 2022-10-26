from django.urls import path, include
from .views import get_all_topics, get_topics_by_category, blog_home

#Blog urls
urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('all_topics', get_all_topics, name = 'all_topics'),
    path('topics_by_category/<str:category>', get_topics_by_category, name='topics_by_category')
]
