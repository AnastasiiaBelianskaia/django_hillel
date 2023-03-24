from django.urls import path

from . import views

app_name = 'math_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('triangle/', views.triangle, name='triangle'),
    path('person/', views.create_entry, name='create_entry'),
    path('person/<int:pk>/', views.edit_entry, name='edit_entry'),
    path('all_users/', views.all_users_list, name='all_users'),
    path('details/<int:pk>/', views.user_details, name='user_details'),
    path('delete_user/<int:pk>/', views.user_delete, name='delete_user'),
]
