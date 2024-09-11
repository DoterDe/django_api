
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from app.views import email_massage,home, DeletePost, CreatePost,APIProductViewSet,APIREADProductViewSet
from rest_framework.routers import DefaultRouter

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
    path('api_product/', include(router.urls)),
    path('api_read', include(router1.urls)),
    # path('api/',APIProduct.as_view(), name='api' ),
    # path('api_id/<int:pk>/', APIProductDetail.as_view(), name='api_id')
]
