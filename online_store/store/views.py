from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import ProductFilter

class MainProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = MainProductSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class BrandViewSets(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand_name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VolumeViewSets(viewsets.ModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['value']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ModelViewSets(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['model_name']
    # permission_classes2 = [permissions.IsAuthenticatedOrReadOnly]


class ColorViewSets(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['color_name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ColorPhotoViewSets(viewsets.ModelViewSet):
    queryset = ColorPhoto.objects.all()
    serializer_class = ColorPhotoSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PhotoViewSets(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['product_name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CharacteristicViewSets(viewsets.ModelViewSet):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', 'key', 'value']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class Carusel_PhotoViewSets(viewsets.ModelViewSet):
    queryset = Carusel_Photo.objects.all()
    serializer_class = Carusel_PhotoSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FavoriteViewSets(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BasketViewSets(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewsViewSets(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class NewsViewSets(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class About_usViewSets(viewsets.ModelViewSet):
    queryset = About_us.objects.all()
    serializer_class = About_usSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
