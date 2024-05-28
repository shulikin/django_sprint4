from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class IsPublishedCreatedAt(models.Model):
    """Класс.BaseModel"""

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
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
        """Класс.Category.Meta"""

        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(IsPublishedCreatedAt):
    """Класс.Location"""

    name = models.CharField(
        'Название места',
        max_length=256
    )

    class Meta:
        """Класс.Location.Meta"""

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
    text = models.TextField('Текст')
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
        related_name='posts',
    )
    location = models.ForeignKey(
        'Location',
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Местоположение',
        related_name='posts',
        null=True,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        related_name='posts',
        null=True,
    )
    image = models.ImageField('Фото', upload_to='post_images', blank=True)

    class Meta:
        """Класс.Post.Meta"""

        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        # ordering = ('-pub_date',)


class Comment(IsPublishedCreatedAt):
    """Класс.Comment"""

    text = models.TextField('Текст')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор публикации',
        related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        verbose_name='Публикация',
        related_name='comments'
    )

    class Meta:
        """Класс.Comment.Meta"""

        verbose_name = 'коментарий'
        verbose_name_plural = 'коментарии'
        ordering = ('created_at',)
