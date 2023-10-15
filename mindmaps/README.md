
# PDF Chatbot with RAG Implementation

This repository contains a chatbot implementation that uses a Retriever-Answerer-Generator (RAG) approach to provide responses based on content extracted from PDF documents.

## Visualization of Module 1 Mind Map

The following code snippet demonstrates how to visualize the mind map for Module 1: Introduction to Chatbots and AI.

```python
# Importing the necessary libraries for visualization
import matplotlib.pyplot as plt
import networkx as nx

# Define the structure for the mind map of Module 1
module_1_edges = [
    ("Module 1: Introduction to Chatbots and AI", "What is a Chatbot?"),
    ("Module 1: Introduction to Chatbots and AI", "AI in Chatbots: A Brief Overview"),
    ("Module 1: Introduction to Chatbots and AI", "Use Cases: Why a PDF Chatbot?")
]

# Creating the directed graph for Module 1 again and visualizing its mind map
G_module_1 = nx.DiGraph()
G_module_1.add_edges_from(module_1_edges)

# Define the layout and visualize the mind map for Module 1
pos_module_1 = nx.spring_layout(G_module_1, seed=42)
plt.figure(figsize=(12, 8))
nx.draw(G_module_1, pos_module_1, with_labels=True, node_size=4000, node_color="lightgreen", font_size=10, width=2, alpha=0.6, edge_color="gray")
plt.title("Module 1: Introduction to Chatbots and AI", size=15)
plt.show()
```

## Requirements

To run the code in this repository, ensure you have the following Python libraries:

- matplotlib
- networkx
- openai
- llama-index
- nltk

## Further Development

Future work on this project will include a deeper RAG implementation, better integration with OpenAI models, and additional features to improve user experience.

## Contributions

Contributions to improve this chatbot or expand its capabilities are welcome. Please submit a pull request or open an issue to discuss proposed changes.

