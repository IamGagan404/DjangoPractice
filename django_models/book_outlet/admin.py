from django.contrib import admin

# Register your models here.

from .models import Book

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("author","is_bestselling",)
    list_display = ("title","author",)

admin.site.register(Book,BookAdmin)


