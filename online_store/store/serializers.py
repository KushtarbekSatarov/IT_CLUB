from rest_framework import serializers
from .models import Product, Color, ColorPhoto, Brand, Volume, Model, Photo, Reviews, Characteristic, Carusel_Photo, Favorite, Basket, Order, News, About_us
from django.contrib.auth.models import User

class ColorPhotoSerializer(serializers.ModelSerializer):
    color_name = serializers.CharField(source='colorphoto_name.color_name', read_only=True)
    color_image = serializers.ImageField(source='colorphoto_image', read_only=True)

    class Meta:
        model = ColorPhoto
        fields = ['colorphoto_name', 'colorphoto_image', 'color_name', 'color_image']

class ColorSerializer(serializers.ModelSerializer):
    color_photo = ColorPhotoSerializer(required=False, allow_null=True)

    class Meta:
        model = Color
        fields = ['color_name', 'color_image', 'color_photo']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['color_photo'] is None:
            del representation['color_photo']
        return representation


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand_name', 'brand_image']


class MainProductSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True)
    colorphoto_image = serializers.SerializerMethodField()
    colorphoto_name = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'colorphoto_image', 'colorphoto_name', 'description', 'colors', 'price', 'stars', 'activate', 'brand']

    def get_colorphoto_image(self, obj):
        color_photos = ColorPhoto.objects.filter(colorphoto_name__in=obj.colors.all())
        return [color_photo.colorphoto_image.url for color_photo in color_photos]

    def get_colorphoto_name(self, obj):
        color_photos = ColorPhoto.objects.filter(colorphoto_name__in=obj.colors.all())
        return [color_photo.colorphoto_name.color_name for color_photo in color_photos]

    def get_brand(self, obj):
        return {
            'brand_name': obj.brand.brand_name,
            'brand_image': obj.brand.brand_image.url.replace('http://localhost:8000', '')
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        colors_data = representation.get('colors', [])
        for color_data in colors_data:
            color_data['color_image'] = color_data['color_image'].replace('http://localhost:8000', '')
            if 'color_photo' in color_data and color_data['color_photo'] is None:
                del color_data['color_photo']
        return representation


class ModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = Model
        fields = ['id', 'model_name', 'brand']


class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ['id', 'value']


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    model = ModelSerializer()
    memory = VolumeSerializer(many=True)

    class Meta:
        model = Product
        # fields = ['id', 'product_name', 'brand', 'model', 'description', 'price', 'date', 'memory', 'stars', 'activate']
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['brand']['brand_image'] = representation['brand']['brand_image'].replace('http://localhost:8000', '')
        return representation


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class ReviewsSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Reviews
        fields = ['user_id', 'user_name', 'reviews', 'stars', 'data', 'product']


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ['id', 'product', 'key', 'value']

class Carusel_PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carusel_Photo
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    user_id  = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Favorite
        fields = ['user_id', 'product']

class BasketSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Basket
        fields = ['user_id', 'product', 'product_count']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class About_usSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_us
        fields = '__all__'

