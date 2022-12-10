"""patterns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from main import views


# V5

urlpatterns = [
    path('', include('main.urls', namespace='book')),
    path('admin/', admin.site.urls),
]


# V4

# urlpatterns = [
#     path('', include('main.urls')),
#     path('admin/', admin.site.urls),
# ]


# V3

# urlpatterns = [
#     path('', views.book_list),
#     path('admin/', admin.site.urls),
# ]


# V2

# urlpatterns = [
#     path('', views.book_list),
#     path('book/<slug:slug>/', views.book_details),
#     path('book/<slug:slug>/add', views.book_add),
#     path('book/<slug:slug>/delete', views.book_delete),
#     path('book/<slug:slug>/edit', views.book_edit),
# ]


# V1

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
