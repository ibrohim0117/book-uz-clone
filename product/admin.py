from django.contrib import admin

from .models import Category, Book, BookImage, Author

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(BookImage)
admin.site.register(Author)

