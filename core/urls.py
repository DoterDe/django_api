from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from app.views import email_massage,home, DeletePost, CreatePost,api_product,api_product_id


urlpatterns = [
    path('admin/', admin.site.urls),
    path('email/' , email_massage, name='email_massage'),
    path('', home, name='home'),
    path('create/', CreatePost.as_view(), name='create'),
    path('delete/<int:id>', DeletePost.as_view(), name='delete'),
    path('api/',api_product, name='api' ),
    path('api_id/<int:pk>/', api_product_id, name='api_id')

]
