from django.contrib import admin
from .models import Category, Book, BookImage, Author


class BookImageInline(admin.StackedInline):
   
    model = BookImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "parent",
        "created_at",
    )
    readonly_fields = ("slug", ) 
    search_fields = ("name",)
    
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "created_at",
    )
    search_fields = ("full_name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "author",
        "category",
        "price",
        "count",
        "is_active",
        "views",
        "created_at",
    )

    

    search_fields = (
        "name",
        "author__full_name",
        "category__name",
    )

    readonly_fields = (
        "views",
        "created_at",
        "updated_at",
    )

    inlines = [BookImageInline]


@admin.register(BookImage)
class BookImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "book",
        "created_at",
    )
    search_fields = ("book__name",)