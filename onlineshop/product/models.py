from django.db import models


class Collection(models.Model):
    title = models.CharField(max_length=100)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL,null = True, blank=True, related_name='featured_product'
    )
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(decimal_places=2)
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(
        Collection, on_delete=models.PROTECT, related_name='products')

class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    


