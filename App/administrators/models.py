# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Django model import:
from django.contrib.auth.models import (
    AbstractBaseUser,
    AbstractUser,
    PermissionsMixin,
    Permission,
    Group,
)


"""class AdministratorPrevisions(models.Model):
    name = models.CharField(_('name'), max_length=150, unique=True)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('permissions'),
        blank=True,
    )"""


"""class Previsions(PermissionsMixin):
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="user_set",
        related_query_name="user",
    )


class Administrator(AbstractUser, Previsions):
    username = models.CharField(_('username'), max_length=64)"""
