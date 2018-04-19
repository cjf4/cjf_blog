from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .forms import CreateReviewForm

def index(request):
	return HttpResponse("No reviews yet!")

def create(request, pk = None):
	if request.method == 'POST':
		#handle review submission logic
		pass
	else:
		if pk is None:
			form = CreateReviewForm()
		else:
			pass
			#get object or 404
			#render the form with the form filled in
	return render(request, 'reviews/create.html', {'form': form})
