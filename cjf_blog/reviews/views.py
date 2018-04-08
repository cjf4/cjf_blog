from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("No reviews yet!")

def create(request):
	return render(request, 'reviews/create.html')
