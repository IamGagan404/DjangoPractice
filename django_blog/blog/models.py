from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    # img_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="uploads/images",null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="posts",null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    

    
class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    datetime = models.DateTimeField(auto_now=True,null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")

    def __str__(self):
        return self.user_name
    








