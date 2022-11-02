

from .forms import RegisterUserForm
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from .models import Author, Category, Topic, Genre
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm




class TopicListView(ListView):
    model = Topic
    context_object_name = 'all_topics'
    template_name = 'blog/all_topics.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['allowed_viewer'] = User.objects.get(pk=1)
        data['all_genres'] = Genre.objects.all()
        return data
    

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/author_detail.html'
    context_object_name = 'author'


# def author_profile(request, author_id):
#     try:
#         author = Author.objects.get(pk=author_id)
#     except:
#         author = None
#     return render(request, 'author/author_detail.html', {'author': author})



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

