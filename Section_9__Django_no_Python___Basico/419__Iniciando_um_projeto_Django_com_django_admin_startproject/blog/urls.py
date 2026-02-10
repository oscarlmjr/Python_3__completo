from blog import views
from django.urls import path

app_name = 'blog'

# blog/
# Django URLs:
# https://docs.djangoproject.com/en/6.0/topics/http/urls/
urlpatterns = [
    path('', views.blog, name='blog'),
	path('post/<int:id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
