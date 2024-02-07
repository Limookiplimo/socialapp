from django.urls import path
from .views import home_page, create_post, delete_post, edit_post, read_post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home_page,name='home'),
    path('post/create/',create_post,name='post-create'),
    path('post/delete/<pk>/',delete_post,name='post-delete'),
    path('post/edit/<pk>/',edit_post,name='post-edit'),
    path('post/read/<pk>/',read_post,name='post-read'),
    path('post/category/<tag>/',home_page,name='post-category'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
