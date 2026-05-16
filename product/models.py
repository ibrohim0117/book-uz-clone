from django.db import models


class BaseCreateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseCreateModel):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    slug = models.SlugField(unique=True, null=False, blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="children")

    def __str__(self):
        return self.name
    
    
class Book(BaseCreateModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    about = models.TextField()
    author = models.IntegerField() 
    count = models.BigIntegerField()
    is_active = models.BooleanField(default=True)
    add_user = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="book_category")
    info = models.JSONField(null=True, blank=True)
    views = models.IntegerField(default=0)

    class Meta:
        db_table = 'book'


class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='books/covers/')
    is_main = models.BooleanField(default=False)  

    def __str__(self):
        return f"Image for {self.book.title}"
    

class BookAuthor(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    about = models.TextField()

    class Meta:
        db_table = 'book_author'
