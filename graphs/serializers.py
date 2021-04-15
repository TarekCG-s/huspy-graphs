from rest_framework import serializers


class ConnectNodesSerializer(serializers.Serializer):
    from_symbol = serializers.CharField()
    to_symbol = serializers.CharField()
