from django.urls import path, include
from .views import *

#Blog urls
urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('all_topics/', TopicListView.as_view(), name = 'all_topics'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author'),
    path('topics_by_category/<str:category>', TopicByCategory.as_view(), name='topics_by_category'),
    path('topic_detail/<int:pk>', TopicDetailView.as_view(), name='topic_detail'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detaul'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    path('author_create/', AuthorCreateView.as_view(), name='author_create'),
    path('author_update/<int:pk>', AuthorUpdateView.as_view(), name='author_update'),
    path('author_delete/<int:pk>', AuthorDeleteView.as_view(), name='author_delete'),
    

]
