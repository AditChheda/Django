from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('register/', views.register, name='register'),
  path('register/register', views.register, name='register2'),
  path('login/', views.login, name='login'),
  path('login/login', views.login, name='login2'),
  path('logout/', views.logout, name='logout'),
  path('profile/', views.profile, name='profile'),
  path('profile/profile', views.profile, name='profile2'),
  ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  