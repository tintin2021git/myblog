from rest_framework import generics
from .serializers import PostSerializer
from .models import Post
# Create your views here.

# Post
class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Post detail
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer