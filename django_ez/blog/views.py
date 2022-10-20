from unicodedata import category
from django.shortcuts import render
from .models import Category, Topic
from django.contrib.auth.models import User


# Create your views here.

def get_all_topics(request):
    all_topics = Topic.objects.all()
    allowed_viewer = User.objects.get(pk=1)



    return render(request, 'blog/all_topics.html', {
        'all_topics': all_topics,
        'allowed_viewer': allowed_viewer,
        })

def get_topics_by_category(request, category):
    #Electronics
    try:
        asked_category = Category.objects.get(title=category)
        topics_by_category = Topic.objects.filter(category=asked_category)
        return render(request, 'blog/get_topics_by_category.html',
        {'topics_by_category': topics_by_category})
    except: # aboba
        return render(request, 'blog/wrong_category.html')

# python manage.py shell
#Author.object.all() - все авторы
#Topic.objects.all() - все топики
#Topic.objects.filter(author=???) - фильтр по автору
# где ??? - это запрос всех авторов + индекс автора
#Topic.objects.filter(author=   Author.objects.all()[1]    )

