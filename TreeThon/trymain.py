import json
from graphviz import Digraph

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

def parse_input(input_str):
    lines = input_str.split('\n')
    root = None
    nodes = {}

    for line in lines:
        parts = line.strip().split(' = ')
        parent_name = parts[0].split('.')[0]
        child_name = parts[1]

        if parent_name == 'root':
            root = Node(child_name)
            nodes[child_name] = root
        else:
            parent_node = nodes[parent_name]
            child_node = Node(child_name)
            parent_node.children.append(child_node)
            nodes[child_name] = child_node

    return root

def tree_to_dot(node, dot):
    dot.node(node.name)
    for child in node.children:
        dot.edge(node.name, child.name)
        tree_to_dot(child, dot)

def main():
    input_str = """root = main
    main.child = child1
    main.child = child3
    child1.child = child2
    main.child = child3
    child3.child = child6"""
    
    root = parse_input(input_str)

    dot = Digraph(comment='Tree')
    tree_to_dot(root, dot)

    directory = "trees_generated"
    filename = input("Enter filename:- ")  #enter filename without extension
    format = "png"
    dot.render(filename, format=format, directory=directory, cleanup=True)

if __name__ == "__main__":
    main()
