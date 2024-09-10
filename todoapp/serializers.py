from rest_framework import serializers
from todoapp.models import Todo

class TodoSerializers(serializers.Serializer):
    class Meta:
        model=Todo
        fields='__all__'
    