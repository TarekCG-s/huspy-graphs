from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import Node
from .serializers import ConnectNodesSerializer


nodes = {}


@api_view(["POST"])
def connect_nodes(request):
    serializer = ConnectNodesSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    from_symbol = data.get("from_symbol")
    to_symbol = data.get("to_symbol")
    from_node = nodes.setdefault(from_symbol, Node(from_symbol))
    to_node = nodes.setdefault(to_symbol, Node(to_symbol))

    from_node.add_adjacent(to_node)
    to_node.add_adjacent(from_node)
    return Response(request.data, status=200)


@api_view(["GET"])
def path(request):
    return Response({}, status=200)
