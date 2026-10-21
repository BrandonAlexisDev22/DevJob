from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from .models import User


class UserReadSerializer(serializers.ModelSerializer):
    """Serializer para la representación pública y segura de un usuario."""

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "phone",
            "role",
            "is_active",
            "created_at",
            "updated_at",
        )
        read_only_fields = fields


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer para la validación y creación de nuevos usuarios."""

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"},
        help_text="Contraseña para la cuenta del usuario.",
    )
    password_confirm = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"},
        help_text="Confirmación de la contraseña.",
    )

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "phone",
            "role",
            "password",
            "password_confirm",
        )

    def validate_email(self, value):
        """Validar normalización e inexistencia previa del correo."""
        email_normalized = value.lower().strip()
        if User.objects.filter(email=email_normalized).exists():
            raise serializers.ValidationError(
                "Ya existe un usuario registrado con este correo electrónico."
            )
        return email_normalized

    def validate(self, attrs):
        """Validación cruzada de contraseñas y fortaleza."""
        password = attrs.get("password")
        password_confirm = attrs.get("password_confirm")

        if password != password_confirm:
            raise serializers.ValidationError(
                {"password_confirm": "Las contraseñas no coinciden."}
            )

        user_temp = User(
            email=attrs.get("email"),
            first_name=attrs.get("first_name"),
            last_name=attrs.get("last_name"),
        )

        try:
            validate_password(password, user=user_temp)
        except DjangoValidationError as error:
            raise serializers.ValidationError({"password": list(error.messages)})

        return attrs

    def create(self, validated_data):
        """Creación del usuario utilizando el CustomUserManager de la app."""
        validated_data.pop("password_confirm", None)
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer():
    pass