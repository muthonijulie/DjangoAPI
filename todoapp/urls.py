from django.urls import path
from todoapp import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns=[
    path('api/',views.todo_list,name='todo_list'),
    path('detail/<int:pk>/',views.todo_detail,name='todo_detail')
]
urlpatterns = format_suffix_patterns(urlpatterns)