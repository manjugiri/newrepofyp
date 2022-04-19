from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, full_name, username, email, password, contact):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            full_name=full_name,
            contact=contact,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_client(self, full_name, email, username, password, contact):

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            full_name=full_name,
            contact=contact,


        )
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, email, username, password, contact):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            full_name=full_name,
            contact=contact
        )

        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    contact = models.IntegerField()

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name', 'contact']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
