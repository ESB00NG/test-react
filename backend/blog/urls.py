from django.urls import path
from .views import PostList, PostDetail, api_root

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('', api_root),  # Añade una vista para /api/
]
