#models.py
from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=100, unique=True)
    brand_image = models.ImageField(upload_to='brand/img/', blank=True, null=True)


    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Model(models.Model):
    model_name = models.CharField(max_length=100, unique=True)
    brand = models.ForeignKey(Brand, related_name='model', on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'


class Volume(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Volume'
        verbose_name_plural = 'Volume'


class Color(models.Model):
    color_name = models.CharField(max_length=40)
    color_image = models.ImageField(upload_to='color/img/')

    def __str__(self):
        return self.color_name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class ColorPhoto(models.Model):
    colorphoto_image = models.ImageField(upload_to='color_photos/img/')
    colorphoto_name = models.OneToOneField(Color, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.colorphoto_name.color_name if self.colorphoto_name else ""

    class Meta:
        verbose_name = 'ColorPhoto'
        verbose_name_plural = 'ColorsPhoto'


class Photo(models.Model):
    image = models.ImageField(upload_to='photo/img/')
    photo_name = models.CharField(max_length=200)

    def __str__(self):
        return self.photo_name

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


class Characteristic(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='characteristics')
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.key} {self.value}'

    class Meta:
        verbose_name = 'Characteristic'
        verbose_name_plural = 'Characteristics'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product_brand')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='product_model')
    description = models.TextField(blank=True, null=True)
    colors = models.ManyToManyField(Color, related_name='product_color', blank=True)
    colorphoto = models.ManyToManyField(ColorPhoto, related_name='product_colorphoto', blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    photos = models.ManyToManyField(Photo, related_name='product_photo', blank=True)
    date = models.DateField(auto_now=True, blank=True, null=True)
    memory = models.ManyToManyField(Volume, related_name='products', blank=True)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name='Grade', blank=True, null=True)
    activate = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product_name} {self.memory}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Carusel_Photo(models.Model):
    photo = models.ImageField(upload_to='carusel/img/')
    title = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Carusel_Photo'
        verbose_name_plural = 'Carusel_Photos'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} | {self.product}'

    class Meta:
        verbose_name ='Favorite'
        verbose_name_plural = 'Favorites'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_basket')
    product_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.user} | {self.product}'

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_amount_order = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user} | {self.product}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class Reviews(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    reviews = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_reviews')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name='Grade')
    data = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.user} | {self.product}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class News(models.Model):
    news_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='news/img/', blank=True, null=True)

    def __str__(self):
        return self.news_name

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'


class About_us(models.Model):
    about_us = models.TextField(verbose_name='About Us')


    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About_Us'