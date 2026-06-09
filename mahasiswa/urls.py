from django.urls import path
from . import views
from django.views.generic import RedirectView

path('', RedirectView.as_view(url='daftar/')),

urlpatterns = [
    path('', views.index, name='index'),
    path('daftar/', views.daftar_mahasiswa, name='daftar_mahasiswa'),
]

