from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API VIEW"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a lis of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to traditional Django view',
            'Gives the most control over application logic',
            'Mapped manually to URLS',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a Hello Message with our Name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )

    def put(self, request, pk=None):
        """Handle Updating Objects"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial object update"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete and object"""
        return Response({'method': 'DELETE'})
