from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.localflavor.us.models import PhoneNumberField, \
                                                 USStateField


class UserProfile(models.Model):
    COLOR_CHOICES = (
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Yellow', 'Yellow'),
        ('Green', 'Green'),
    )
    user = models.ForeignKey(User)
    favorite_color = models.CharField(
        max_length=255,
        choices=COLOR_CHOICES,
        null=True, blank=True)
    phone = PhoneNumberField(blank=True, null=True)
    state = USStateField(blank=True, null=True)


