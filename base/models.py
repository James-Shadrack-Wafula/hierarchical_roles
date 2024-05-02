from django.db import models
from django.contrib.auth.models import AbstractUser

# from django.contrib.auth.models import AbstractUser
# from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Seller', 'Seller'),
    )
    user_role = models.CharField(max_length=10, choices=ROLES)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set'  
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set'  
    )

class Manager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.user.username

class Seller(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.user.username
   