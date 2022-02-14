from rest_framework                             import serializers
from vuelosApp.models.user                      import User
from vuelosApp.models.tarjetas                  import Tarjetas
from vuelosApp.serializers.tarjetasSerializer   import TarjetasSerializer

class UserSerializer(serializers.ModelSerializer):
    tarjetas = TarjetasSerializer()
    class Meta:
        model  = User
        fields = ["id_user", "username", "nombres", "apellidos", "password", "correo", "tarjetas"]
    
    def create(self, validated_data):
        tarjetaData  = validated_data.pop('tarjetas')
        userInstance = User.objects.create(**validated_data)
        Tarjetas.objects.create(cliente = userInstance, **tarjetaData)

        return userInstance
    
    def to_representation(self, instance):                          # lo que se va a mostrar en la respuesta del frontend. Es la respuesta del postman
        user     = User.objects.get(id_user = instance.id_user)
        tarjetas = Tarjetas.objects.get(cliente = user.id_user) 
        return {
                "id_user"        : user.id_user,
                "username"       : user.username,
                "nombres"        : user.nombres,
                "apellidos"      : user.apellidos,
                "correo"         : user.correo,
                "tarjetas": {
                            "id_tarjeta"         : tarjetas.id_tarjetas,
                            "nombre_propietario" : tarjetas.nombre_propietario,
                            "tipo"               : tarjetas.tipo
                }               
        }
