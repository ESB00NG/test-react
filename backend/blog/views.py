from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Lista de posts y creación de nuevos posts
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Detalle, actualización y eliminación de un post
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Vista de la raíz de la API
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Blog API. Navigate to /api/posts/ to see the posts."
    })
