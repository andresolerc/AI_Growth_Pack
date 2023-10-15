

# Mind Map Visualization for Module 1

This Python script visualizes a mind map for "Module 1: Introduction to Chatbots and AI" using `matplotlib` and `networkx`.

## Prerequisites

- Python
- `matplotlib` and `networkx` libraries

You can install the required libraries using:

```bash
pip install matplotlib networkx
```

## How it Works

1. **module_1_edges**: This list defines the relationships (edges) between the main module topic and its subtopics.
2. **G_module_1**: This is a directed graph created using `networkx` that represents the mind map.
3. **pos_module_1**: This determines the layout of the nodes in the visualization. The `spring_layout` ensures a visually appealing arrangement.
4. The visualization is then rendered using `matplotlib` with customized node sizes, colors, and other properties to enhance readability.

## Usage

Simply run the script to view the mind map for "Module 1: Introduction to Chatbots and AI". The visualization displays the main topic and its associated subtopics, showcasing their relationship.
