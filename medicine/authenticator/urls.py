from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('results/', views.results, name='results'),
    path('upload/', views.upload, name='upload')
]