from django.urls import path

from . import views

urlpatterns = [
    # path("",views.review)
    path("",views.ReviewView.as_view()),
    path("thankyou",views.thankyou),
    path("reviews",views.ReviewsListView.as_view()),
    path("reviews/<int:pk>",views.SingleView.as_view())
]
