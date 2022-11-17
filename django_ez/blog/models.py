
from django.db import models
from django.utils import timezone




class Topic(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', unique=True)
    content = models.TextField(max_length=1000, verbose_name='Текст статьи')
    author = models.ForeignKey('Author', on_delete=models.PROTECT, verbose_name='Автор')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Предпросмотр фото')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория', unique=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    nickname = models.CharField(max_length=100, blank=True, verbose_name='Ник')
    genre = models.ForeignKey('Genre', on_delete = models.CASCADE, blank=True, null=True, verbose_name='Жанр')
    birthday = models.DateField(default=timezone.now(), verbose_name='Дата рождения')
    country = models.ForeignKey('Country', on_delete = models.CASCADE, blank=True, null=True, verbose_name='Страна') #если страна больше не поддерживается, удаляем всех авторов, потом хочу переделать


    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return "/blog/author/%i" % self.id

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'



class Genre(models.Model):
    title = models.CharField(max_length=100, verbose_name='Жанр')
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Country(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название страны')
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural ='Страны'