from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def account_confirm_email(request, key):
    return render(request, 'auth/confirm_email.html')


def password_reset_confirm(request, uidb64, token):
    return HttpResponse(uidb64, token)
