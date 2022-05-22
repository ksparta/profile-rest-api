from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API VIEW"""

    def get(self, request, format=None):
        """Returns a lis of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to traditional Django view',
            'Gives the most control over application logic',
            'Mapped manually to URLS',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    