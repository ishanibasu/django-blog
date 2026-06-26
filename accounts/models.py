from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    photo = models.ImageField(
        upload_to='users/%Y/%m/%d/',
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    github = models.URLField(
        blank=True
    )

    linkedin = models.URLField(
        blank=True
    )

    instagram = models.URLField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    def __str__(self):
        return f'Profile of {self.user.username}'