from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from todoapp.models import Todo
from todoapp.serializers import TodoSerializers

@api_view(['GET','POST'])
def todo_list(request,format=None):
    if request.method=='GET':
        todo=Todo.objects.all()
        serializer=TodoSerializers(todo,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=TodoSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
     
@api_view(['GET','PUT','DELETE'])
def todo_detail(request,pk,format=None):
    try:
        todo=Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response('Todo Unavailable', status=404)
    if request.method=='GET':
        serializer=TodoSerializers(todo)
        return Response(serializer.data)
    elif request.method=='PUT':
       
        serializer=TodoSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
