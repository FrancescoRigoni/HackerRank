#!/usr/bin/python

"""
Link: https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
"""


class Graph:
    def __init__(self, nodes):
        self.nodes_count = nodes;
        self.adjacencies = dict((node, []) for node in range(nodes))

    def connect(self, start, end):
        if self.adjacencies[start] is None:
            self.adjacencies[start] = []
        if self.adjacencies[end] is None:
            self.adjacencies[end] = []
        # Connect start to end and end to start (undirected graph)
        self.adjacencies[start].append(end)
        self.adjacencies[end].append(start)

    def visit_frontier(self, frontier, frontier_distance, visited_list, distances, new_frontier):
        for node in frontier:
            if node not in visited_list:
                visited_list.append(node)
                distances[node] = frontier_distance
                new_frontier.extend(self.adjacencies[node])

    def find_all_distances(self, start):
        visited_list = []
        distances = dict()

        frontier = [start]
        frontier_distance = 0

        while len(frontier) > 0:
            new_frontier = []
            self.visit_frontier(frontier, frontier_distance, visited_list, distances, new_frontier)
            frontier_distance += 1
            frontier = new_frontier

        distances_string = ""
        for node in range(nodes):
            if node != start:
                if node in distances:
                    distances_string += str(distances[node]*6) + " "
                else:
                    distances_string += "-1 "

        print(distances_string.strip())


with open("input.txt") as f:
    content = f.readlines()

t = int(content.pop(0))
for i in range(t):
    nodes, edges = [int(value) for value in content.pop(0).split()]
    graph = Graph(nodes)
    for e in range(edges):
        edge_start, edge_end = [int(x) for x in content.pop(0).split()]
        graph.connect(edge_start - 1, edge_end - 1)
    start_node = int(content.pop(0))
    graph.find_all_distances(start_node - 1)


