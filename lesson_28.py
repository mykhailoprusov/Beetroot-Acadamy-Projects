from typing import List
import copy
# 0 - Kyiv
# 1 - London
# 2 - Lviv
# 3 - Glasgow
# 4 - Paisley

# I tried to implement Kosaraju Algorithm here

class Graph:
    def __init__(self,vertices):

        self.vertices = vertices
        self.graph = [[0] * vertices for i in range(vertices)]
        self.vertices_words = {0:'Kyiv',1:'London',2:'Lviv',3:'Glasgow',4:'Paisley'}

    def add_edge(self,first_vertex,second_vertex):
        self.graph[first_vertex][second_vertex] = 1

    def print_matrix(self):
        for row in self.graph:
            print(row)

    def dfs(self, start):
        visited = set()
        storage = []
        stack = [start]

        while stack:

            vertex = stack.pop()
            if vertex not in visited:

                visited.add(vertex)
                storage.append(vertex)
                print(vertex)

                for neighbor_idx, neighbor in enumerate(self.graph[vertex]):
                    if neighbor == 1 and neighbor_idx not in visited:
                        stack.append(neighbor_idx)

        return visited,storage

    def transpose(self):

        graph_transpose = [[0] * self.vertices for i in range(self.vertices)]
        graph_for_iteration = copy.deepcopy(self.graph)

        for i in self.graph:
            for j in i:
                if j == 1:

                    index = graph_for_iteration[self.graph.index(i)].index(j)
                    graph_for_iteration[self.graph.index(i)][index] = 0
                    graph_transpose[index][self.graph.index(i)] = 1

        print(graph_transpose)
        return graph_transpose

    def scc(self,transposed_graph: List ,all_vertices: List, start: int, str_c_c: List, index_scc=0,visited_= set()):

        visited = visited_
        stack = [start]
        strong_con_comp = str_c_c
        index = index_scc
        strong_con_comp.insert(index,[])

        while stack:
            vertex = stack.pop()
            if vertex not in visited:

                visited.add(vertex)
                strong_con_comp[index].append(vertex)

                print(vertex)

                for neighbor_idx, neighbor in enumerate(transposed_graph[vertex]):
                    if neighbor == 1 and neighbor_idx not in visited:
                        stack.append(neighbor_idx)

        if len(all_vertices) != visited:
            
            for i in all_vertices:
                if i not in visited:
                    new_start = i
                    index+=1
                    strong_con_comp = self.scc(transposed_graph, all_vertices, new_start, str_c_c,index,visited)

        return strong_con_comp




if __name__ == '__main__':
    graph = Graph(5)

    graph.add_edge(0,1)

    graph.add_edge(1,2)

    graph.add_edge(2,0)
    graph.add_edge(2,3)

    graph.add_edge(3,4)

    graph.add_edge(4,3)

    graph.print_matrix()

    visited,visited_lst = graph.dfs(0)

    transpose = graph.transpose()

    result = graph.scc(transpose,visited_lst,0,[])

    print(result)

