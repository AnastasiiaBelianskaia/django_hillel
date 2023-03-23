from django.urls import path

from . import views

app_name = 'math_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('triangle/', views.triangle, name='triangle'),
    path('person/', views.create_entry, name='create_entry'),
    path('person/<int:pk>/', views.edit_entry, name='edit_entry'),
    path('person/created/<int:pk>/', views.created_entry, name='created_entry'),
    path('person/edited/<int:pk>', views.edited_entry, name='edited_entry'),
]
