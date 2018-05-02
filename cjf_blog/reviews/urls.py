from django.urls import path
from . import views


app_name = 'reviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('all_reviews', views.review_list, name='review_list')
]