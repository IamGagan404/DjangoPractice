from django.shortcuts import render
from .form import ReviewForm
from django.views import View
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import FormView,CreateView
# Create your views here.

def thankyou(request):
    return render(request,"reviews/thankyou.html")

# class ReviewView(View):
#     def get(self,request):
#         form = ReviewForm()
#         return render(request,"reviews/review.html",{
#         "form": form
#     })

#     def post(self,request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # review = Review(user_name=form.cleaned_data['user_name'],feedback=form.cleaned_data['review_text'],rating=form.cleaned_data['rating'])
#             # review.save()
#             form.save()
#             return render(request, "reviews/thankyou.html")
#         return render(request,"reviews/review.html",{
#         "form": form
#     })

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thankyou"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class ReviewView(FormView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thankyou"


# def review(request):
#     if request.method == "POST": 
#         form = ReviewForm(request.POST) # get data from form, 'instance' keyword to update existing entry
#         if form.is_valid():
#             print(form.cleaned_data)
#             # review = Review(user_name=form.cleaned_data['user_name'],feedback=form.cleaned_data['review_text'],rating=form.cleaned_data['rating'])
#             # review.save()
#             form.save()
#             return render(request, "reviews/thankyou.html")
#     else:
#         form = ReviewForm()

#     return render(request,"reviews/review.html",{
#         "form": form
#     })


# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] =  reviews
#         return context
    
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # get_queryset method used for filter objects
    # add .filter to base query in super

    

# class SingleView(TemplateView):
#     template_name = "reviews/single.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         review = Review.objects.get(pk=review_id)
#         context["review"] =  review
#         return context
    

class SingleView(DeleteView):
    template_name = "reviews/single.html"
    model = Review

