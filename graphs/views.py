from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import Node, PathFinding
from .serializers import NodesSerializer

import json


nodes = {}


@api_view(["POST"])
def connect_nodes(request):
    """
    HTTP Endpoint used for connecting nodes in graph.
    """

    serializer = NodesSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    from_node = data.get("from_node")
    to_node = data.get("to_node")
    from_node = nodes.setdefault(from_node, Node(from_node))
    to_node = nodes.setdefault(to_node, Node(to_node))

    from_node.add_adjacent(to_node)
    to_node.add_adjacent(from_node)
    return Response(request.data, status=201)


@api_view(["GET"])
def path(request):
    """
    HTTP Endpoint used for searching for shortest path between two nodes in graph.
    """

    from_node = request.GET.get("from_node")
    if not from_node:
        return Response({"error": "from_node query parameter is required."}, status=400)

    from_node = nodes.get(from_node)
    if not from_node:
        return Response({"error": "This from_node doesn't exist"}, status=400)

    to_node = request.GET.get("to_node")
    if not to_node:
        return Response({"error": "to_node query parameter is required."}, status=400)

    to_node = nodes.get(to_node)
    if not to_node:
        return Response({"error": "This to_node doesn't exist"}, status=400)

    path_finder = PathFinding(from_node, to_node)
    path = path_finder.traverse()
    if not path:
        return Response(
            {"path": f"There's no path between nodes {from_node} - {to_node}"},
            status=200,
        )

    path = ", ".join(path)
    return Response({"path": path}, status=200)
