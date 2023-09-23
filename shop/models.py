from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

User = get_user_model()
class Category(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField()

    def __str__(self):
        return self.title
class Product(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "products"
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop')

    def __str__(self):
        return self.product.title
