
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from app.views import email_massage,home, DeletePost, CreatePost,APIProductViewSet,APIREADProductViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache

from core.settings import DEBUG
from app.views import Login

router = DefaultRouter()
router.register('product', APIProductViewSet)
router1 = DefaultRouter()
router1.register('product1', APIREADProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('email/' , email_massage, name='email_massage'),
    path('', home, name='home'),
    path('create/', CreatePost.as_view(), name='create'),
    path('delete/<int:id>', DeletePost.as_view(), name='delete'),
    # path('api/',api_product, name='api' ),
    # path('api_id/<int:pk>/', api_product_id, name='api_id'),
    path('login/' , Login.as_view(), name='login' ),
    path('api_product/', include(router.urls)),
    path('api_read', include(router1.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/',APIProduct.as_view(), name='api' ),
    # path('api_id/<int:pk>/', APIProductDetail.as_view(), name='api_id')
]
if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
