from django.db import models

# Create your models here.
class Price(models.Model):
    topwear = models.IntegerField(default='25')
    bottomwear = models.IntegerField(default='25')
    woolenwear = models.IntegerField(default='25')

    def __str__(self):
        return str(self.topwear)
    
class Company(models.Model):
    comapny_name = models.CharField(max_length=100, default='laundry')
    comapny_email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    fav_icon = models.ImageField(upload_to='company_fav_icons/', blank=True, null=True)

    def __str__(self):
        return str(self.comapny_name)
