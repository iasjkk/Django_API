from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class info(models.Model):
    # def __init__(self, id, last_name, first_name, email_id, city):
    #     self.id= id
    #     self.last_name=last_name
    #     self.first_name =first_name
    #     self.email_id=email_id
    #     self.city=city
    id  = models.CharField(max_length=100, primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
