from django.db import models

# Create your models here.


class Thread(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=500)
    text = models.CharField('Текст поста', max_length=500)
    number = models.IntegerField(default=0)
    image = models.ImageField(
        'Картинка',
        blank=True,
        null=True,
        help_text='Загрузите картинку'
    )
    thread = models.ForeignKey(
        Thread,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='thread',
        verbose_name='Тред',
        help_text='Тред, к которой будет относиться пост'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-number']

    def __str__(self):
        return self.title

