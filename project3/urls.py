
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='product_home'),
    path('account/', include('account.url')),
    path('product/', include('product.url')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
