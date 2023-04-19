from django.urls import path
from . import views

# LIBRARY APP
urlpatterns  = [
    path('', view.index, name='index')
    path('/books', views.get_all_books, name='books')
]

# USERS APPSAS
urlpatterns = [
    path('', views.user_index, name='user_index_page')
    path('<int:user_id>/', views.get_one_user, name='some_user')
]