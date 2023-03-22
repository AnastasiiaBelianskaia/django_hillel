from django.urls import path

from . import views

app_name = 'math_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('triangle/', views.triangle, name='triangle'),
]
