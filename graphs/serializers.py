from rest_framework import serializers


class NodesSerializer(serializers.Serializer):
    from_node = serializers.CharField()
    to_node = serializers.CharField()
