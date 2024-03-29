from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("<h1>This is home page of users</h1>")


def users(request):
    return HttpResponse("<h1>This page for users\n</h1>"
                        + "Foydalanuvchining shaxsiy <a href='https://t.me/Abu_MuhammadSodiq_MuhammadYusuf'> kabineti</a>")

