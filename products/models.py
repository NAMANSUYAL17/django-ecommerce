from django.db import models

# Create your models here.
class   Category((models.Model)):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=120,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural="Categories"
    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=220,unique=True)
    description=models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-created_at']
    def __str__(self):
        return self.name
