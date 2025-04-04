from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import  MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                           MaxValueValidator(70)],
                                    null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    user_image = models.ImageField(upload_to="images/", null=True, blank=True)
    STATUS_CHOICES = (
        ('gold', 'gold'),
        ('simple', 'simple'),
        ('bronze', 'bronze'),
        ('silver', 'silver'),
    )
    status = models.CharField(choices=STATUS_CHOICES, default='simple', max_length=16)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)


    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  related_name='category_products')
    product_name = models.CharField(max_length=64)
    article = models.PositiveIntegerField(unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    check_original = models.BooleanField(default=False)
    product_video = models.FileField(upload_to="product_video/", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="product_photo/")


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductPhoto, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f'{self.user}, {self.stars}'


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.product}'