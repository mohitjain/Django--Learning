from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Returns a list of API View features"""
        an_apiview = [
            'Uses HTTP methods as function (get post, path, put, delete)',
            'Is similiar to a traditional Django View',
            'Gives you th emost control over the application logic',
            'Is Mapped manually to URLS'
        ]

        return Response({'message': "Hello", 'as_apiview': an_apiview})
