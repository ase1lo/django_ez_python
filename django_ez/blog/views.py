

from .forms import RegisterUserForm
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from .models import Author, Category, Topic, Genre
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import Http404



class AuthorCreateView(CreateView): #как создать что-то с сайта
    model = Author
    fields = ['name', 'nickname', 'genre', 'country', 'birthday',]
    template_name = 'author/author_form.html'



class CategoryCreateView(CreateView):
    model = Category
    fields = ['title',]
    template_name = 'category/category_form.html'


class TopicListView(ListView): # ListView - objecst.all() objects.filter() - queryset
    model = Topic
    context_object_name = 'all_topics'
    template_name = 'blog/all_topics.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['allowed_viewer'] = User.objects.get(pk=1)
        data['all_genres'] = Genre.objects.all()
        return data
    

class AuthorDetailView(DetailView): # detailView - single object objects.get() 
    model = Author
    template_name = 'author/author_detail.html'
    context_object_name = 'author'

    def get(self, request, *args, **kwargs):
        self.request_author = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['topics'] = Topic.objects.filter(author=self.request_author)
        print(data)

        return data


class TopicByCategory(ListView):
    model = Topic
    template_name = "blog/get_topics_by_category.html"
    context_object_name = "topics_by_category"

    def get(self, request, *args, **kwargs): # blog/topic_byt_category/Python - Python (конец url) - получаем из
        request_category = kwargs['category']  # из метода get 
        try:
            self.category_id = Category.objects.get(title=request_category).id
        except:
            raise Http404("Url does not exist") 
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['topics_by_category'] = Topic.objects.filter(category=self.category_id)
        return data


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'topic/topic_detail.html'
    context_object_name = 'topic'


def blog_home(request):
    return render(request, 'blog/blog_home.html')
    

def get_topics_by_category(request, category):
    #Electronics
    try:
        asked_category = Category.objects.get(title=category)
        topics_by_category = Topic.objects.filter(category=asked_category)
        return render(request, 'blog/get_topics_by_category.html',
        {'topics_by_category': topics_by_category})
    except: # aboba
        return render(request, 'blog/wrong_category.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm #модель формы forms.py
    template_name = 'auth/register.html'
    success_url = '/blog'


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('blog_home')   #переадресация







# python manage.py shell
#Author.object.all() - все авторы
#Topic.objects.all() - все топики
#Topic.objects.filter(author=???) - фильтр по автору
# где ??? - это запрос всех авторов + индекс автора
#Topic.objects.filter(author=   Author.objects.all()[1]    )

