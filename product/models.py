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
    
    
class Product(BaseCreateModel):
    pass

