from rest_framework import serializers
from todoapp.models import Todo
from django.contrib.auth.models import User

class TodoSerializers(serializers.HyperlinkedModelSerializer):
    task_by = serializers.ReadOnlyField(source='task_by.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='todo-highlight', format='html')

    class Meta:
        model = Todo
        fields = ['url', 'id', 'title','highlight', 
                   'content', 'created_at','task_by']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    todo = serializers.HyperlinkedRelatedField(many=True, 
    view_name='todo-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'todo']