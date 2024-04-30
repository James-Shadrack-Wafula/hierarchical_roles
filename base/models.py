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
        related_name='custom_user_set'  # Specify a related_name
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set'  # Specify a related_name
    )

class Manager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add other manager-specific fields as needed

class Seller(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add other seller-specific fields as needed

    # Your custom fields and logic here

    # class Meta:
    #     permissions = models.ManyToManyField(
    #         'auth.Permission',
    #         verbose_name='user permissions',
    #         blank=True,
    #         related_name='customuser_user_permissions',
    #         related_query_name='user'
    #     )
        # groups = models.ManyToManyField(
        #     'auth.Group',
        #     verbose_name='groups',
        #     blank=True,
        #     help_text=(
        #         'The groups this user belongs to. '
        #         'A user will get all permissions granted to each of their groups.'
        #     ),
        #     related_name='customuser_groups',
        #     related_query_name='user'
        # )
        # Add unique related_name arguments
        # You can use any unique names that make sense for your application
        # Here, I'm using 'customuser_groups' and 'customuser_user_permissions'
        # permissions = models.ManyToManyField(
        #     Permission,
        #     verbose_name=_('user permissions'),
        #     blank=True,
        #     related_name='customuser_user_permissions',
        #     related_query_name='user'
        # )
        # groups = models.ManyToManyField(
        #     Group,
        #     verbose_name=_('groups'),
        #     blank=True,
        #     help_text=_(
        #         'The groups this user belongs to. '
        #         'A user will get all permissions granted to each of their groups.'
        #     ),
        #     related_name='customuser_groups',
        #     related_query_name='user'
        # )