import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
nuremberg_metro = nx.Graph()

# Додавання станцій та ребер
nuremberg_metro.add_edge("Plärrer", "Hauptbahnhof")
nuremberg_metro.add_edge("Plärrer", "Weißer Turm")
nuremberg_metro.add_edge("Plärrer", "Wöhrder Wiese")
nuremberg_metro.add_edge("Hauptbahnhof", "Lorenzkirche")
nuremberg_metro.add_edge("Hauptbahnhof", "Opernhaus")
nuremberg_metro.add_edge("Hauptbahnhof", "Kaulbachplatz")
nuremberg_metro.add_edge("Weißer Turm", "Lorenzkirche")
nuremberg_metro.add_edge("Lorenzkirche", "Opernhaus")
nuremberg_metro.add_edge("Opernhaus", "Henkersteg")
nuremberg_metro.add_edge("Wöhrder Wiese", "Rathenauplatz")
nuremberg_metro.add_edge("Rathenauplatz", "Maxfeld")
nuremberg_metro.add_edge("Maxfeld", "Friedrich-Ebert-Platz")
nuremberg_metro.add_edge("Friedrich-Ebert-Platz", "Bärenschanze")
nuremberg_metro.add_edge("Bärenschanze", "Thon")

# Візуалізація графа
pos = nx.spring_layout(nuremberg_metro)  # позиції вершин для графа

# Розміщення вершин та ребер
nx.draw(nuremberg_metro, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")
nx.draw_networkx_edge_labels(nuremberg_metro, pos, font_color="gray", font_size=8)

# Відображення графа
plt.title("Карта метро Нюрнберга")
plt.axis("off")
plt.show()
