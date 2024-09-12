from todoapp.models import Todo
from todoapp.serializers import TodoSerializers,UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from todoapp.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from django.contrib.auth.models import User
from rest_framework import permissions



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'todo': reverse('todo-list', request=request, format=format)
    })
class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
class TodoHighlight(generics.GenericAPIView):
    queryset = Todo.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        todo = self.get_object()
        return Response(todo.highlighted)
      
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        
        serializer.save(task_by=self.request.user)
        


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.http import Http404
# from todoapp.models import Todo
# from todoapp.serializers import TodoSerializers


# class Todo_list(APIView):
#     def get(self,request,format=None):
#         todo=Todo.objects.all()
#         serializer=TodoSerializers(todo,many=True)
#         return Response(serializer.data)
    
#     def post(self,request,format=None):
#         serializer=TodoSerializers(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
        
#         return Http404

# class Todo_detail(APIView):
#     def get(self,pk):
#         try:
#            todo=Todo.objects.get(pk=pk)
#         except Todo.DoesNotExist:
#            return Response('Todo Unavailable', status=404)
#     def get(self,request,pk,format=None):
#         todo=self.get_object(pk)
#         serializer=TodoSerializers(todo)
#         return Response(serializer.data)
#     def put(self,request,pk,format=None):
       
#         serializer=TodoSerializers(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_HTTP_404_NOT_FOUND)
        
#         return Http404
#     def delete(self,request,pk,format=None):
#         todo = self.get_object(pk)
#         todo.delete()
#         return Http404
