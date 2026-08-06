from django.shortcuts import render
from .fetch_data import fetch_data
from django.http import HttpResponse


# Create your views here.
def test_db(request):
    fetch_data()
    return HttpResponse("printed on terminal")