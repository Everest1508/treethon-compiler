# TreeThon Compiler

## Overview
TreeThon is a simple language for representing hierarchical data structures in a text-based format. This compiler translates TreeThon code into JSON format, allowing you to visualize and work with hierarchical data more easily.

## Features
- Parses TreeThon code into a hierarchical tree structure
- Converts the tree structure into JSON format

## Getting Started
To use the TreeThon compiler, follow these steps:

1. **Install Python**: Ensure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the TreeThon compiler code:

    ```
    git clone https://github.com/Everest1508/treethon-compiler.git
    ```

3. **Navigate to the Directory**: Go to the directory where the code is cloned:

    ```
    cd treethon-compiler
    ```

4. **Run the Compiler**: Execute the compiler script with your TreeThon code as input:

    ```
    python TreeThon/main.py
    ```

5. **View the Output**: The compiler will generate JSON output representing the hierarchical structure defined in your TreeThon code.

## Syntax
TreeThon syntax follows a simple key-value pair format, where the key represents the parent node and the value represents the child node:

parent_node = child_node


Nodes are separated by newline characters, and each line defines a relationship between parent and child nodes.

## Example
Consider the following TreeThon code:

```
root = main
main.child = child1
main.child = child3
child1.child = child2
main.child = child3
child3.child = child6```


This code defines a hierarchical structure with the "main" node as the root, having two children ("child1" and "child3"), and further children branching off from them. When compiled, this code will produce the corresponding JSON representation.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
