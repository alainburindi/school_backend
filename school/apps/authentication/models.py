import uuid
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.URLField(
        default='https://res.cloudinary.com/health-id/image/upload/'
        'v1554552278/Profile_Picture_Placeholder.png'
    )
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
