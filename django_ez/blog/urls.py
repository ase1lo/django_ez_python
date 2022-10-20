from django.urls import path, include
from .views import get_all_topics, get_topics_by_category

#Blog urls
urlpatterns = [
    path('all_topics', get_all_topics, name = 'all_topics'),
    path('topics_by_category/<str:category>', get_topics_by_category, name='topics_by_category')
]
