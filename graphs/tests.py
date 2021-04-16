from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory


class GraphsTest(APITestCase):
    """
    Test Class for testing different scenarios for graph traversal.
    """

    def test_connect_nodes(self):
        """
        Test connecting two nodes endpoint.
        """
        data = {"from_node": "A", "to_node": "B"}
        response = self.client.post(reverse("graphs:connect-node"), data, format="json")
        from .views import nodes

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(nodes), 2)

    def test_get_path(self):
        """
        Test scenario to get the path between two nodes.
        """
        self.client.post(
            reverse("graphs:connect-node"),
            {"from_node": "A", "to_node": "B"},
            format="json",
        )
        self.client.post(
            reverse("graphs:connect-node"),
            {"from_node": "B", "to_node": "C"},
            format="json",
        )
        response = self.client.get(
            reverse("graphs:path"), {"from_node": "A", "to_node": "C"}
        )
        resp_data = response.json()
        self.assertEqual(resp_data.get("path"), "A, B, C")

    def test_get_shortest_path(self):
        """
        Scenario tests having two possible paths between two nodes.
        Should return the shortest path.
        """
        self.client.post(
            reverse("graphs:connect-node"),
            {"from_node": "A", "to_node": "B"},
            format="json",
        )
        self.client.post(
            reverse("graphs:connect-node"),
            {"from_node": "B", "to_node": "C"},
            format="json",
        )
        self.client.post(
            reverse("graphs:connect-node"),
            {"from_node": "A", "to_node": "C"},
            format="json",
        )
        response = self.client.get(
            reverse("graphs:path"), {"from_node": "A", "to_node": "C"}
        )
        resp_data = response.json()
        self.assertEqual(resp_data.get("path"), "A, C")

    def test_non_existent_path(self):
        """
        Scenario tests looking up for a path between unconnected node.
        Should not return a path.
        """
        self.client.post(
            reverse("graphs:connect-node"),
            {"from_node": "A", "to_node": "B"},
            format="json",
        )
        self.client.post(
            reverse("graphs:connect-node"),
            {"from_node": "D", "to_node": "F"},
            format="json",
        )
        response = self.client.get(
            reverse("graphs:path"), {"from_node": "A", "to_node": "F"}
        )
        resp_data = response.json()
        self.assertEqual(resp_data.get("path"), "There's no path between nodes A - F")
