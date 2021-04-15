class Node:
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
        return f"{self.symbol}"

    def __eq__(self, item):
        if isinstance(item, self.__class__):
            return self.symbol == item.symbol
        return False


class TraverseUnit:
    def __init__(self, node, parent):
        self.node = node
        self.parent = parent

    def __repr__(self):
        return f"({self.node} - {self.parent})"

    def __str__(self):
        return f"{self.node} - {self.parent}"

    def __eq__(self, item):
        if isinstance(item, self.__class__):
            return self.node == item.node
        return False


class TraverseQueue:
    def __init__(self):
        self.queue = []

    def add(self, unit):
        self.queue.append(unit)

    def contains_unit(self, new_unit):
        return any(unit == new_unit for unit in self.queue)

    def empty(self):
        return len(self.queue) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty queue")
        else:
            unit = self.queue[0]
            self.queue = self.queue[1:]
            return unit


class PathFinding:
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        self._traverse_queue = TraverseQueue()
        self._explored_units = []
        self._traverse_queue.add(TraverseUnit(self.from_node, None))

    def traverse(self):
        while not self._traverse_queue.empty():
            cur_unit = self._traverse_queue.remove()
            self._explored_units.append(cur_unit)

            if cur_unit.node == self.to_node:
                path = [cur_unit.node.symbol]
                while cur_unit.parent:
                    cur_unit = cur_unit.parent
                    path.append(cur_unit.node.symbol)
                path.reverse()
                return path

            else:
                units_to_explore = map(
                    lambda adj: TraverseUnit(adj, cur_unit), cur_unit.node.adjacents
                )
                filtered_units = filter(
                    lambda unit: not self._traverse_queue.contains_unit(unit)
                    and unit not in self._explored_units,
                    units_to_explore,
                )

                for unit in filtered_units:
                    self._traverse_queue.add(unit)
        return []
