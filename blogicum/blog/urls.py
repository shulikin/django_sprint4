from django.urls import path

from . import views

app_name = 'blog'


urlpatterns = [
    path(  # category
        'category/<slug:category_slug>/',
        views.PostCategoryView.as_view(),
        name='category_posts'
    ),
    path(  # профиль пользователь
        'profile/<str:username>/',
        views.ProfileListView.as_view(),
        name='profile'
    ),
    path(  # профиль редактировать
        'edit_profile/',
        views.ProfileUpdateView.as_view(),
        name='edit_profile'
    ),
    path(  # публикация
        'posts/<int:post_id>/',
        views.PostDetailView.as_view(),
        name='post_detail'
    ),
    path(  # публикация добавить
        'posts/create/',
        views.PostCreateView.as_view(),
        name='create_post'
    ),
    path(  # публикация редактировать
        'posts/<int:post_id>/edit/',
        views.PostUpdateView.as_view(),
        name='edit_post'
    ),
    path(  # публикация удалить
        'posts/<int:post_id>/delete/',
        views.PostDeleteView.as_view(),
        name='delete_post'
    ),
    path(  # Комментарий добавить
        'posts/<int:post_id>/comment/',
        views.CommentCreateView.as_view(),
        name='add_comment'
    ),
    path(  # Комментарий редактировать
        'posts/<int:post_id>/edit_comment/<int:comment_id>/',
        views.CommentUpdateView.as_view(),
        name='edit_comment'
    ),
    path(  # Комментарий удалить
        'posts/<int:post_id>/delete_comment/<int:comment_id>/',
        views.CommentDeletView.as_view(),
        name='delete_comment'
    ),
    path(
        '',
        views.PostListView.as_view(),
        name='index'),
]
