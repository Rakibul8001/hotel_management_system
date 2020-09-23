from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='This is default description')
    hotel_main_image = models.ImageField(upload_to = 'images/')
    price = models.IntegerField(default=1000)
    offer = models.BooleanField(default = False)

    def __str__(self):
        return self.name
