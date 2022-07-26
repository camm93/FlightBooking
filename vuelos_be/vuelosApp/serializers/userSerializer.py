from rest_framework import serializers
from vuelosApp.models.user import User
from vuelosApp.models.tarjeta import Tarjeta
from vuelosApp.serializers.tarjetaSerializer import TarjetaSerializer


class UserSerializer(serializers.ModelSerializer):

    tarjeta = TarjetaSerializer()

    class Meta:
        model  = User
        fields = ["username", "first_name", "last_name", "password", "email", "tarjeta"]

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs["username"]).exists()
        if username_exists:
            raise serializers.ValidationError(detail="User with username already exists")

        email_exists = User.objects.filter(username=attrs["email"]).exists()
        if email_exists:
            raise serializers.ValidationError(detail="User with email already exists")

        return super().validate(attrs)

    def create(self, validated_data):
        tarjetaData = validated_data.pop('tarjeta')
        if not tarjetaData.get("nombre_propietario"):
            tarjetaData["nombre_propietario"] = f"{validated_data.get('first_name')} {validated_data.get('last_name')}"
        userInstance = User.objects.create(**validated_data)
        Tarjeta.objects.create(cliente=userInstance, **tarjetaData)
        return userInstance

    def to_representation(self, instance):
        user = User.objects.get(id_user=instance.id_user)
        tarjeta = Tarjeta.objects.get(cliente=user.id_user)
        return {
            "id_user": user.id_user,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "tarjeta": {
                "id_tarjeta": tarjeta.id_tarjeta,
                "nombre_propietario": tarjeta.nombre_propietario,
                "tipo": tarjeta.tipo
            }
        }
