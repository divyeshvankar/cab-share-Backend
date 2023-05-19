from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BookViewSet(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
