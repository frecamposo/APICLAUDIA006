from rest_framework import serializers;
from .models import Receta

# definir los modelos
class RecetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = "__all__"
        
