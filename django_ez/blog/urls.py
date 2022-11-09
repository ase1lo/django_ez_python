from django.urls import path, include
from .views import get_topics_by_category, blog_home, TopicListView, AuthorDetailView, TopicByCategory

#Blog urls
urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('all_topics', TopicListView.as_view(), name = 'all_topics'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author'),
    path('topics_by_category/<str:category>', TopicByCategory.as_view(), name='topics_by_category')
]
