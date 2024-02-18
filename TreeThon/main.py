import json

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

def tree_to_json(node):
    json_tree = {
        "name": node.name,
        "children": [tree_to_json(child) for child in node.children]
    }
    return json_tree

def main():
    input_str = """root = main
    main.child = child1
    main.child = child3
    child1.child = child2
    main.child = child3
    child3.child = child6"""
    root = parse_input(input_str)

    json_tree = tree_to_json(root)
    compiled_data ="["+json.dumps(json_tree)+"]"
    mymain = []
    mymain.append(json_tree)
    print(mymain)

if __name__ == "__main__":
    main()
