from distutils.command.upload import upload
from email.mime import image
from pyexpat import model
from time import strftime
from django.db import models
import datetime
import os

def get_file_path(request, filename):
    original_filename = filename
    now = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (now, original_filename)
    return os.path.join('uploads/', filename)


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    status = models.BooleanField(default=False, help_text='0=default, 1=hidden')
    trending = models.BooleanField(default=False, help_text='0=default, 1=trending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    product_desciption = models.TextField(null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    product_status = models.BooleanField(default=False, help_text='0=default, 1=hidden')
    product_trending = models.BooleanField(default=False, help_text='0=default, 1=trending')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.product_name