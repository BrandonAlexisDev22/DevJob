from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Manager personalizado donde el email es el identificador único."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("El campo Email debe ser obligatorio"))
        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("El superusuario debe tener is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("El superusuario debe tener is_superuser=True."))

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Modelo de Usuario personalizado para DevJob utilizando email como credencial principal."""

    class Role(models.TextChoices):
        DEVELOPER = "DEVELOPER", _("Developer")
        COMPANY = "COMPANY", _("Company")

    # Deshabilitamos el campo username heredado de AbstractUser
    username = None

    # Credenciales y Campos Obligatorios
    email = models.EmailField(_("correo electrónico"), unique=True, db_index=True)
    first_name = models.CharField(_("nombre"), max_length=30)
    last_name = models.CharField(_("apellido"), max_length=30)

    # Campos Opcionales
    phone = models.CharField(
        _("número de teléfono"),
        max_length=20,
        unique=True,
        null=True,
        blank=True,
    )

    # Autorización y Estado
    role = models.CharField(
        _("rol"),
        max_length=20,
        choices=Role.choices,
        default=Role.DEVELOPER,
        db_index=True,
    )
    is_active = models.BooleanField(default=True)

    # Marcas de tiempo (Auditoría)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = _("usuario")
        verbose_name_plural = _("usuarios")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.email} ({self.role})"