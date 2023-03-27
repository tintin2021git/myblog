from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import BlogSerializer
from .models import Blog
# Create your views here.

# blog
class BlogListView(ListAPIView):
    queryset = Blog.objects.order_by('-create_at')
    serializer_class = BlogSerializer

# blog detail
class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer