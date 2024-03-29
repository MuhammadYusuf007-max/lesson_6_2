from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("<h1>This is home page of library</h1>")


def books(request):
    return HttpResponse("<h1>This page for books\n</h1>"
                        + "Musulmonning 35 odobi Abdulfattoh Abu G'udda tomonidan yozilgan.<a href='https://t.me/misbah_ilm/355'> Taqriz</a>")
