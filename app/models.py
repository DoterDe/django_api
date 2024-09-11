from django.db import models
from django.contrib.auth.models import User




class UserProfile(User):
    cv = models.FileField(upload_to='cv/photos')
    photo = models.ImageField(upload_to ='photo/photos' )
    id_photo = models.ImageField(upload_to = 'id_photo/photos')
    def __str__(self) -> str:
        return f'{self.first_name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def str(self):
        return self.name