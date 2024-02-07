from django.urls import path
from .views import profile_page, edit_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/',profile_page, name='profile'),
    path('profile/edit',edit_profile, name='profile-edit'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
