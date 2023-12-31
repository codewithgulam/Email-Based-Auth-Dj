from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin, BaseUserManager, UserManager

# Create your CustomUserManager models here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        if not email:
            raise ValueError("Email is not Provided")
        if not password:
            raise ValueError("Password is not Provided")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name= last_name,
            mobile=mobile,
            **extra_fields
        )
        user.set_password(password)
        user.save(using= self.db)
        return user
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


# Create your User models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True,unique=True, max_length=254)
    first_name =models.CharField( max_length=50)
    last_name =models.CharField( max_length=50)
    mobile =models.CharField( max_length=50)
    address =models.CharField( max_length=50)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name', 'mobile']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

