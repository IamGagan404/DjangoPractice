from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Addresses"




class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])  
    # author = models.CharField(null=True,max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True,null=False,db_index=True) # for performance
    published_country = models.ManyToManyField(Country,null=False)


    def get_absolute_url(self):
        return reverse("book_details_page", args=[self.slug])
    
    # def save(self, *args, **kwargs):

    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.title} ({self.rating})"

