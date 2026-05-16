import uuid
from django.db import models
from django.utils.text import slugify


class BaseCreateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Category(BaseCreateModel):
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, editable=False)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="children", blank=True, null=True)
    category_image = models.ImageField(upload_to="category/", null=True, blank=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        self.slug = slug
        while Category.objects.filter(slug=slug).exists():
            addon = uuid.uuid4().hex[2]
            slugger = f"{slug}-{addon}"
            self.slug = slugger
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class Author(BaseCreateModel):
    full_name = models.CharField(400)
    about = models.TextField()

    def __str__(self):
        return self.full_name


class Book(BaseCreateModel):
    name = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    about = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField(default=True)
    add_user = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="category", blank=True, null=True)
    info = models.JSONField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")
    views = models.IntegerField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        self.slug = slug
        while Book.objects.filter(slug=slug).exists():
            addon = uuid.uuid4().hex[2]
            slugger = f"{slug}-{addon}"
            self.slug = slugger
        return super().save(*args, **kwargs)
    


class BookImage(BaseCreateModel):
    image = models.ImageField(upload_to="books/")
    book  = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_image")

    def __str__(self):
        return self.book.name


