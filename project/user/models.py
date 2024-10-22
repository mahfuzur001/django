from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class Customer(AbstractUser):
    phone_no=models.CharField(max_length=10)
    billing_address=models.CharField(max_length=100)
    shipping_address=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='profile_pic/')
    dob=models.DateField()

    
    # Override groups and user_permissions to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Provide unique related_name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Provide unique related_name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions"
    )
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'