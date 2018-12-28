
"""
This file is general brushing up on  graphs from a CS standpoint
a-f are vertices
The connecting line between two nodes is called an edge. and cann be displayed ad a tuple

 If the edges between the nodes have no direction(undirected) , the graph is called an undirected graph. If an edge is directed from one vertex ( or  node) to another, graph is  a directed graph. A directed edge is called an arc.

 An isolated vertex (or node) is one that has no edges

"""


a_through_f_graph = {
    "a": ["c"],
    "b": ["c","e"],
    "c": ["a","b","d","e"],
    "d": ["d"],
    "e": ["b","c"],
    "f": []
}


def generate_edges(graph):
    edges = [] # An empty array to store the edges
    # This loops through the graph dictionary to get access to all of the graphs vertices and edges (keys and list, values)
    for node in graph:
        for neighbour in graph[node]:  # This loop through the list of values at the key
            edges.append((node, neighbour)) #in a tuple, this adds the current node as well as each edge for that node to the edges list
    return edges

def vertices_and_list_of_edge(graph):
    for key,value in graph.items():
        print('vertex is : {} \n they link to: {} '.format(key,value))

def isolated_vertices(graph):
    isolated_nodes = [] # Make an empty list to store nodes that are isolated
    for node,neighbors in graph.items(): # need both the key and the values for appending to the list
        if not neighbors: # if the neighbors is an empty list (aka it connects to nothing)
            isolated_nodes.append(node) # Add that to the list
    return isolated_nodes



def main():
    # print(vertices_and_list_of_edge(a_through_f_graph))
    # print(generate_edges(a_through_f_graph))
    print(isolated_vertices(a_through_f_graph))


if __name__ == "__main__":
    main()
