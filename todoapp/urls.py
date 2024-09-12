from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('api/', views.api_root),
    path('api/users/',views.UserList.as_view(), name='user-list'),
    path('api/users/detail/<int:pk>',views.UserDetail.as_view(), name='user-detail'),
    path('api/todo',views.TodoList.as_view(),name='todo-list'),
    path('api/todo/detail/<int:pk>/',views.TodoDetail.as_view(),name='todo-detail'),
    path('api/todo/<int:pk>/highlight/', views.TodoHighlight.as_view(),name='todo-highlight')
]
)