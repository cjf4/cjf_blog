from django.urls import path
from . import views


app_name = 'reviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('all_reviews', views.ReviewListView.as_view(), name='review_list'),
    path('review/<int:pk>', views.ReviewDetailView.as_view(), name = 'review-detail')
]