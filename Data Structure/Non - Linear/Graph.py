# Graph non-linear , recursive data structure
# ( vertices and edges ) edges : can be weighted
# 1.    Directed Graph  e.g. flight routes
# 2.    Un-Directed Graph  e.g. FB friends

class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                paths.extend(self.get_paths(start=node, end=end, path=path))
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path

    def get_min_stops(self, start, end, path=[]):
        list_of_paths = self.get_paths(start, end, path)
        return min([len(path) for path in list_of_paths])

    def get_shortest_path_new(self, start, end, path=[]):
        list_of_paths = self.get_paths(start, end, path)

        min_stops = list_of_paths[0]
        for idx, path in enumerate(list_of_paths):
            if len(path) < len(min_stops):
                min_stops = path
        return min_stops


if __name__ == '__main__':
    routes = [
        ('mumbai', 'paris'),
        ('mumbai', 'dubai'),
        ('paris', 'dubai'),
        ('paris', 'new york'),
        ('dubai', 'new york'),
        ('new york', 'toronto'),
    ]

    routes_graph = Graph(edges=routes)
    start = 'mumbai'
    end = 'dubai'

    print(f"Routes between {start} and {end} : ", routes_graph.get_paths(start, end))
    print(f"Min stops between {start} and {end} : ", routes_graph.get_min_stops(start, end))
    print(f"Shortest path between {start} and {end} : ", routes_graph.get_shortest_path_new(start, end))
