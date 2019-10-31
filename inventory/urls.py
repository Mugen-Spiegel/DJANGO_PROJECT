"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
# from django.urls import path, include, re_path
from store import views
urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('admin/', admin.site.urls),
    path('store', views.store),
    path('products', views.products),
    path(r'products/<int:store_id>/<int:product_id>', views.storeProdAvailability),
    path(r'products/inventory', views.updateStoreStock),
    path(r'store/products', views.addStoreProductStock), #This End point is addional this is to add existing product to store
]


# username:tamay06131993@gmail.com
# password:jophattamayo
# grant_type:client_credentials
# client_id:F6NRnSNt1GhHTSLc26AEvOcA0uZ5c15JztTmhNEL
# client_secret:PdAMiWuvkq8VvzqqnMGulPjTGkbV58L86arAV8Oiwqe0UePQLuET3OFT962wXxFjPBsBSHBP8F7eqzhjpSBTqCNJOhilOxC39nZPM1hEGax5BDKXhwCAjzDp4YO2tQmv