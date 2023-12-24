
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from apps.product import api

router = DefaultRouter()
router.register(r'category',api.CategoryApiView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
]
