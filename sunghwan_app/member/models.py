from django.db import models
from django.contrib.auth.models \
    import User, BaseUserManager, UserManager, AbstractBaseUser, PermissionsMixin
from django.conf import settings
import os


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, full_name, nickname, phonenumber, image=None,is_sunghwan=False,):

        if not image:
            image = os.path.join(settings.STATIC_DIR, 'images/default-user.png')

        user = self.model(
            username=username,
            full_name=full_name,
            nickname=nickname,
            phonenumber=phonenumber,
            is_sunghwan=is_sunghwan,
            image=image
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, full_name, nickname, phonenumber, image=None,is_sunghwan=True,):

        if not image:
            image = os.path.join(settings.STATIC_DIR, 'images/default-user.png')

        user = self.model(
            username=username,
            full_name=full_name,
            nickname=nickname,
            phonenumber=phonenumber,
            is_sunghwan=True,
            image=image,
            is_staff =True

        )
        user.set_password(password)
        user.is_superuser=True
        user.save()

        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):

    # essential information
    username = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photo', blank=True, null=True)
    phonenumber = models.CharField(max_length=15)

    # sunghwan or not
    is_sunghwan = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    # manager
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'nickname', 'phonenumber']

    def get_full_name(self):
        return '%s' % (self.full_name)


    def get_short_name(self):
        return self.nickname


