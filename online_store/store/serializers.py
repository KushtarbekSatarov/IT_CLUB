from rest_framework import serializers
from .models import Product, Color, ColorPhoto, Brand, Volume, Model, Photo, Reviews, Characteristic, Carusel_Photo, Favorite, Basket, Order, News, About_us

class ColorPhotoSerializer(serializers.ModelSerializer):
    color_name = serializers.CharField(source='colorphoto_name.color_name', read_only=True)
    color_image = serializers.ImageField(source='colorphoto_image', read_only=True)

    class Meta:
        model = ColorPhoto
        fields = ['colorphoto_name', 'colorphoto_image']
class ColorSerializer(serializers.ModelSerializer):
    # color_photo = ColorPhotoSerializer(required=False, allow_null=True)

    class Meta:
        model = Color
        fields = ['color_name', 'color_image']
        ref_name = 'Color'  # Set a distinct ref_name


class MainProductSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True)
    colorphoto_image = serializers.SerializerMethodField()
    colorphoto_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['product_name', 'colorphoto_image', 'colorphoto_name', 'description', 'colors', 'price', 'stars', 'activate', 'brand_id']

    def get_colorphoto_image(self, obj):
        color_photos = ColorPhoto.objects.filter(colorphoto_name__in=obj.colors.all())
        request = self.context.get('request')
        base_url = request.build_absolute_uri('/')[:-1]  # Remove trailing slash
        return [base_url + color_photo.colorphoto_image.url for color_photo in color_photos]

    def get_colorphoto_name(self, obj):
        color_photos = ColorPhoto.objects.filter(colorphoto_name__in=obj.colors.all())
        return [color_photo.colorphoto_name.color_name for color_photo in color_photos]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        colors_data = representation.get('colors', [])
        request = self.context.get('request')
        for color_data in colors_data:
            color_instance = Color.objects.filter(color_name=color_data['color_name']).first()
            if color_instance:
                color_data['color_image'] = request.build_absolute_uri(color_instance.color_image.url)
            else:
                color_data.pop('color_image', None)  # Remove 'color_image' key if color_instance is None
        return representation



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'

class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'

class Carusel_PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carusel_Photo
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'

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
