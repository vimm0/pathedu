# from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.user.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    STAFF_TYPE = (
        ('COUNSELLOR', 'COUNSELLOR'),
        ('TEACHER', 'TEACHER'),
    )
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('middle name'), max_length=30, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=30)

    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_(''))
    is_active = models.BooleanField(_('active'), default=True, help_text=_(''))
    staff_type = models.CharField(max_length=80, choices=STAFF_TYPE, null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = "Users"
