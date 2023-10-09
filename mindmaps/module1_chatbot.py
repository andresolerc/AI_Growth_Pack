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
