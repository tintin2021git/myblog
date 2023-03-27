from rest_framework import serializers
from .models import Blog

# blog
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'