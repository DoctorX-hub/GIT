from django.db import models

# Create your models here.
class Ip_list(models.Model):
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    type = models.BooleanField()
class User_code(models.Model):
    code = models.CharField(max_length=10)