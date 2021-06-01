from django.urls import path, include, reverse
from main import views



# V4
app_name= 'book'

urlpatterns = [
    path('', views.index),
    path('book/<slug:slug>/', views.book_detail, name='detail')
]


# V3

# urlpatterns = [
#     path('', views.book_list),
#     path('book/<slug:slug>/', views.book_detail)
# ]


# V2

# urlpatterns = [
#     path('', views.book_list),
#     path('book/<slug:slug>/', include([
#         path('', views.book_detail),
#         path('add', views.book_add),
#         path('delete', views.book_delete),
#         path('edit', views.book_edit),
#     ])),
# ]


# V1 on project patterns' urls.py