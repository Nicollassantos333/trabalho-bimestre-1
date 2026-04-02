from django.shortcuts import render, redirect
from django.http import HttpResponse
from polls.forms import pergunta
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = pergunta(request.POST)
        if form.is_valid():