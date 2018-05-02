from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Review

from .forms import CreateReviewForm

def index(request):
	num_reviews = Review.objects.all().count()

	return render(
		request,
		'reviews/index.html',
		context = {'num_reviews': num_reviews}
		)

def review_list(request):
	all_reviews = Review.objects.all()

	return render(
		request,
		'reviews/all_reviews.html',
		context = {'all_reviews': all_reviews})

def about(request):
	return render(request, 'about.html')





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
