class Node():
    def __init__(self, symbol):
        self.symbol = symbol
        self.adjacents = []

    def add_adjacent(self, node):
        if node not in self.adjacents and node != self:
            self.adjacents.append(node)
        return True

    def __repr__(self):
        return f"Node {self.symbol}"

    def __str__(self):
        return f"Node {self.symbol}"

    def __eq__(self, item):
        if isinstance(item, self.__class__):
            return self.symbol == item.symbol
        return False
