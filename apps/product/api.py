from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Category
from .serializers import CategorySerializer



class CategoryApiView(viewsets.ViewSet):
    """
    A simple ViewSet for viewing all categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        print(self.queryset)
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
    