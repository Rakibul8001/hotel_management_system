from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('upload/', views.imageUpload, name = 'upload'),
    path('success/', views.success, name='success'),
]
