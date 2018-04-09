import copy
from pprint import pprint


class SkiMap(object):
    graph = {}

    test = {1: {"connections": [], "name": "Red 4a"},
            2: {"connections": [], "name": "Arei"}}

    def add_node(self, node_name, node_id=None):
        if not node_id:
            try:
                node_id = max(list(self.graph.keys())) + 1
            except ValueError:
                node_id = 1

        self.graph[node_id] = {"name": node_name}

    def print_nodes(self):
        pprint(self.graph)

    def connect_nodes(self, start_node, end_node):
        current_connections = self.graph[start_node].get("connections", [])
        current_connections.append(end_node)

        self.graph[start_node]["connections"] = current_connections

    def get_all_paths(self, start_node, end_node):
        return self.all_paths(self.graph, start_node, end_node)

    def get_shortest_paths(self, start_node, end_node):
        shortest = None

        for path in self.all_paths(self.graph, start_node, end_node):
            if not shortest or len(path) < len(shortest):
                shortest = path

        return shortest

    def all_paths(self, graph, start, end, path=[]):
        temp_path = copy.deepcopy(path)
        temp_path.append(start)

        if start == end:
            return [temp_path]

        paths = []
        for node in graph[start].get("connections", []):
            if node not in temp_path:
                new_paths = self.all_paths(graph, node, end, temp_path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def print_path_in_text(self, shortest):
        text = ""
        for step in shortest:
            text = text + " -> {}".format(self.graph[step].get("name", "UNKNOWN"))

        print(text)
