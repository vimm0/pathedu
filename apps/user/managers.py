from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):

    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        user = self.model(username=username,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, is_staff=False, **extra_fields):
        return self._create_user(username, password, is_staff, False, **extra_fields)

    def create_superuser(self, username, password, is_staff=True, **extra_fields):
        return self._create_user(username, password, is_staff, True, **extra_fields)
