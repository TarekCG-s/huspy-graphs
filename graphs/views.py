
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def connect_nodes(request):
    return Response(request.data, status=200)

@api_view(['GET'])
def path(request):
    return Response({}, status=200)
 
