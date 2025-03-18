from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Username", max_length=20, error_messages={
#         "required":"Username can not be empty",
#         "max_length":"Shorter name pls"
#     })

#     review_text = forms.CharField(label="Your Feedback",widget=forms.Textarea, max_length=100)
#     rating = forms.IntegerField(label="Your Rating",min_value=1,max_value=10)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name','feedback','rating'] # or '__all__' to render all 
        # exclude = []
        labels = {
            "user_name" : "Your Name",
            "feedback": "Your Feedback",
            "rating" : "Your Rating"
        }
        error_messages = {}   # for custom msgs

