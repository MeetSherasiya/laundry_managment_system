from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)


class UserReqeuest(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_date = models.DateField()
    topwear = models.PositiveIntegerField(default=0)
    bottomwear = models.PositiveIntegerField(default=0)
    woolenwear = models.PositiveIntegerField(default=0)
    otherclothes = models.PositiveIntegerField(default=0)

    #service Choices
    SERVICE_CHOICES = [
        ('drop', 'Drop'),
        ('pickup', 'House Pickup'),
    ]
    service_type = models.CharField(max_length=10, choices=SERVICE_CHOICES)
    address = models.TextField(null=True, blank=True)
    contact_person = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    PROGRESS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accept', 'Accept'),
        ('Inprogress', 'Inprogress'),
        ('Finish', 'Finish'),
        ('Cancle', 'Cancle'),
    ]
    progress = models.CharField(max_length=10, choices=PROGRESS_CHOICES)
    topwearprice = models.PositiveIntegerField(default=0)
    bottomwearprice = models.PositiveIntegerField(default=0)
    woolenwearprice = models.PositiveIntegerField(default=0)
    otherclothesprice = models.PositiveIntegerField(default=0)
    totalprice = models.PositiveIntegerField(default=0)
    PAYMENT_CHOICES = [
        ('Unpaid', 'Unpaid'),
        ('Cash', 'Cash'),
        ('Online', 'Online')
    ]
    payment = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
