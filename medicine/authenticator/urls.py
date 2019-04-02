from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('upload-form/', views.upload_form, name='upload-form'),
    # path('upload-excel/', views.upload_excel, name='upload-excel')
]