from django.urls import path,include
from .views import *

urlpatterns = [

    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path("dj-rest-auth/google/login/", GoogleLoginView.as_view(), name="google_login"),
    # path("~redirect/", view=UserRedirectView.as_view(), name="redirect"),


    path('mainproduct/', MainProductViewSets.as_view({'get': 'list'}),
         name='main_list'),
    path('mainproduct/<int:pk>/', MainProductViewSets.as_view({'get': 'retrieve'}),
         name='main_detail'),

    path('brand/', BrandViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='brand_list'),
    path('brand/<int:pk>/', BrandViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete':  'destroy'}),
         name='brand_detail'),

    path('volume/', VolumeViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='volume_list'),
    path('volume/<int:pk>/', VolumeViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='volume_detail'),

    path('model/', ModelViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='marka_list'),
    path('model/<int:pk>/', ModelViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete':  'destroy'}),
         name='model_detail'),

    path('product/', ProductViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='product_list'),
    path('product/<int:pk>/', ProductViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete':  'destroy'}),
         name='product_detail'),

    path('favorite/', FavoriteViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='favorite_list'),
    path('favorite/<int:pk>/', FavoriteViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete':  'destroy'}),
         name='favorite_detail'),

    path('basket/', BasketViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='Basket_list'),
    path('basket/<int:pk>/', BasketViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete':  'destroy'}),
         name='Basket_detail'),

    path('order/', OrderViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='order_list'),
    path('order/<int:pk>/', OrderViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete':  'destroy'}),
         name='order_detail'),

    path('news/', NewsViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='news_list'),
    path('news/<int:pk>/', NewsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete':  'destroy'}),
         name='news_detail'),

    path('about_us/', About_usViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='about_us_list'),
    path('about_us/<int:pk>/', About_usViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete':  'destroy'}),
         name='about_us_detail'),

    path('color/', ColorViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='color_list'),
    path('color/<int:pk>/', ColorViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='color_detail'),

    path('reviews/', ReviewsViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='reviews_list'),
    path('reviews/<int:pk>/', ReviewsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='reviews_detail'),

    path('carusel_photo/', Carusel_PhotoViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='carusel_photo_list'),
    path('carusel_photo/<int:pk>/', Carusel_PhotoViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='carusel_photo_detail'),

    path('photo/', PhotoViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='photo_list'),
    path('photo/<int:pk>/', PhotoViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='photo_detail'),

    path('characteristic/', CharacteristicViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='characteristic_list'),
    path('characteristic/<int:pk>/', CharacteristicViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='characteristic_detail'),
]