from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .form import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# Create your views here.

def store_file(file):
    with open("temp/image.jpg","wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html",{
#             "form": form
#         })

#     def post(self, request):
#         sub_form = ProfileForm(request.POST, request.FILES)
#         if sub_form.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             # store_file(request.FILES["image"])
#             return HttpResponseRedirect("/profiles")
#         return render(request,"profiles/create_profile.html",{
#             "form" : sub_form
#         })



