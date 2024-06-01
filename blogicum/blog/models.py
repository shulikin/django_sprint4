from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class IsPublishedCreatedAt(models.Model):
    """Класс.BaseModel"""

    is_published = models.BooleanField(
        'Опубликовано',
        default=True,

    )
    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True,
    )

    class Meta:
        """Класс.BaseModel.Meta"""

        abstract = True


class Category(IsPublishedCreatedAt):
    """Класс.Category"""

    title = models.CharField(
        'Заголовок',
        max_length=256
    )
    description = models.TextField('Описание')
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text=(
            'Идентификатор страницы для URL; разрешены символы'
            ' латиницы, цифры, дефис и подчёркивание.'
        ),
    )

    class Meta:

        verbose_name = "категория"
        verbose_name_plural = "Категории"
        ordering = ("title",)

    def __str__(self):
        return self.title


class Location(IsPublishedCreatedAt):
    """Класс.Location"""

    name = models.CharField(
        'Название места',
        max_length=256
    )

    class Meta:

        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Post(IsPublishedCreatedAt):
    """Класс.Post"""

    title = models.CharField(
        'Заголовок',
        max_length=256
    )
    text = models.TextField(
        'Текст',
    )
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем'
            ' — можно делать отложенные публикации.'
        ),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        'Location',
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Местоположение',

        null=True,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        verbose_name='Категория',

        null=True,
    )
    image = models.ImageField('Фото', upload_to='post_images', blank=True)

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"
        default_related_name = "posts"
        ordering = ("-pub_date",)

    def __str__(self):
        return self.title


class Comment(IsPublishedCreatedAt):
    text = models.TextField('Текст',)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        verbose_name='Публикация',
    )

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "Комментарии"
        default_related_name = "comments"
        ordering = ("created_at",)

    def __str__(self):
        return f"Комментарий {self.author}"
