"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from blog import views as blog_views
from django.contrib import admin
from django.urls import include, path
# from home import views as home_views

# http://dominio.com.br/
# http://127.0.0.1:8000/
# http://127.0.0.1:8000
# http://127.0.0.1:8000/blog
# http://127.0.0.1:8000/blog/
# http://127.0.0.1:8000/blog/articles/
# http://127.0.0.1:8000/blog/articles/comments
# http://127.0.0.1:8000/blog/articles/categories
# http://127.0.0.1:8000/blog/articles/authors

urlpatterns = [
    # path('', home_views.home),
    path('', include('home.urls')),
    # path('blog/', blog_views.blog),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
