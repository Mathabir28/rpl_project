# from urllib import request
# from django.http import HttpResponse

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Mahasiswa


def index(request):
    context = {
        'judul': 'Halo Mahasiswa',
        'deskripsi': 'Contoh halaman index menggunakan Django templates dan static files.'
    }
    return render(request, 'mahasiswa/index.html', context)
# Create your views here.

@login_required(login_url='/accounts/login/')
def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()
    return render(request, 'mahasiswa/daftar.html', {'mahasiswas': mahasiswas})

# def index(request):
#     return HttpResponse("Hello, ini modul praktikum RPL Django!")