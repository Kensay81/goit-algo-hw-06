import networkx as nx
import matplotlib.pyplot as plt

# Создание пустого графа
transport_graph = nx.Graph()

# Добавление станций метро
metro_stations = [
    ("Hauptbahnhof", {"pos": (0, 0)}),
    ("Plärrer", {"pos": (1, 1)}),
    ("Weißer Turm", {"pos": (2, 2)}),
    ("Opernhaus", {"pos": (3, 3)}),
    ("Fürth Hauptbahnhof", {"pos": (0, 1)}),
    ("Rothenburger Straße", {"pos": (1, 0)}),
    ("Bauernfeindstraße", {"pos": (4, 4)}),
    ("Eberhardshof", {"pos": (5, 5)}),
    ("Frankenstraße", {"pos": (6, 6)}),
    ("Gostenhof", {"pos": (7, 7)}),
    ("Gustav-Adolf-Straße", {"pos": (8, 8)}),
    ("Hallplatz", {"pos": (9, 9)}),
    ("Herrnhütte", {"pos": (10, 10)}),
    ("Hohe Marter", {"pos": (11, 11)}),
    ("Jakobinenstraße", {"pos": (12, 12)}),
    ("Langwasser Nord", {"pos": (13, 13)}),
    ("Langwasser Mitte", {"pos": (14, 14)}),
    ("Langwasser Süd", {"pos": (15, 15)}),
    ("Lorenzkirche", {"pos": (16, 16)}),
    ("Maffeiplatz", {"pos": (17, 17)})
]

transport_graph.add_nodes_from(metro_stations)

# Добавление станций трамвайных линий
tram_stations = [
    ("Am Wegfeld", {"pos": (3, 0)}),
    ("Friedrich-Ebert-Platz", {"pos": (3, 1)}),
    ("Marientor", {"pos": (3, 2)}),
    ("Rennweg", {"pos": (3, 4)}),
    ("Doku-Zentrum", {"pos": (3, 5)}),
    ("Dutzendteich", {"pos": (3, 6)}),
    ("Doku-Zentrum", {"pos": (3, 5)}),
    ("Tiergärtnertor", {"pos": (3, 7)}),
    ("Plärrer", {"pos": (1, 1)}),  # Станция, общая для метро и трамваев
    ("Maxfeld", {"pos": (1, 3)}),
    ("Dürrenhof", {"pos": (1, 4)}),
    ("Fabrikstraße", {"pos": (1, 5)}),
    ("Bauernfeindstraße", {"pos": (4, 4)}),  # Станция, общая для метро и трамваев
    ("Eberhardshof", {"pos": (5, 5)}),  # Станция, общая для метро и трамваев
    ("Erlenstegen", {"pos": (5, 6)}),
    ("Dianaplatz", {"pos": (5, 7)}),
    ("Veilhofstraße", {"pos": (5, 8)}),
    ("Thon", {"pos": (5, 9)}),
    ("Am Wegfeld", {"pos": (3, 0)})  # Станция, общая для метро и трамваев
]

transport_graph.add_nodes_from(tram_stations)

# Добавление рёбер метро (с указанием расстояний)
metro_edges = [
    ("Hauptbahnhof", "Plärrer", {"distance": 1000, "mode": "metro", "line": "U1"}),
    ("Plärrer", "Weißer Turm", {"distance": 800, "mode": "metro", "line": "U1"}),
    ("Weißer Turm", "Opernhaus", {"distance": 600, "mode": "metro", "line": "U1"}),
    ("Opernhaus", "Hauptbahnhof", {"distance": 1200, "mode": "metro", "line": "U1"}),
    ("Hauptbahnhof", "Fürth Hauptbahnhof", {"distance": 5000, "mode": "metro", "line": "U2"}),
    ("Fürth Hauptbahnhof", "Rothenburger Straße", {"distance": 4000, "mode": "metro", "line": "U2"}),
    ("Rothenburger Straße", "Hauptbahnhof", {"distance": 4500, "mode": "metro", "line": "U2"}),
    ("Bauernfeindstraße", "Eberhardshof", {"distance": 1000, "mode": "metro", "line": "U3"}),
    ("Eberhardshof", "Frankenstraße", {"distance": 800, "mode": "metro", "line": "U3"}),
    ("Frankenstraße", "Gostenhof", {"distance": 600, "mode": "metro", "line": "U3"}),
    ("Gostenhof", "Gustav-Adolf-Straße", {"distance": 1200, "mode": "metro", "line": "U3"}),
    ("Gustav-Adolf-Straße", "Hallplatz", {"distance": 5000, "mode": "metro", "line": "U3"}),
    ("Hallplatz", "Herrnhütte", {"distance": 4000, "mode": "metro", "line": "U3"}),
    ("Herrnhütte", "Hohe Marter", {"distance": 4500, "mode": "metro", "line": "U3"}),
    ("Hohe Marter", "Jakobinenstraße", {"distance": 1000, "mode": "metro", "line": "U3"}),
    ("Jakobinenstraße", "Langwasser Nord", {"distance": 800, "mode": "metro", "line": "U3"}),
    ("Langwasser Nord", "Langwasser Mitte", {"distance": 600, "mode": "metro", "line": "U3"}),
    ("Langwasser Mitte", "Langwasser Süd", {"distance": 1200, "mode": "metro", "line": "U3"}),
    ("Langwasser Süd", "Lorenzkirche", {"distance": 5000, "mode": "metro", "line": "U3"}),
    ("Lorenzkirche", "Maffeiplatz", {"distance": 4000, "mode": "metro", "line": "U3"}),
    ("Maffeiplatz", "Hauptbahnhof", {"distance": 4500, "mode": "metro", "line": "U3"})
]
transport_graph.add_edges_from(metro_edges)

# Добавление рёбер трамвайных линий (с указанием расстояний)
tram_edges = [
    ("Hauptbahnhof", "Plärrer", {"distance": 1500, "mode": "tram", "line": "T1"}),
    ("Plärrer", "Maxfeld", {"distance": 700, "mode": "tram", "line": "T1"}),
    ("Maxfeld", "Am Wegfeld", {"distance": 1000, "mode": "tram", "line": "T1"}),
    ("Plärrer", "Friedrich-Ebert-Platz", {"distance": 500, "mode": "tram", "line": "T2"}),
    ("Friedrich-Ebert-Platz", "Marientor", {"distance": 800, "mode": "tram", "line": "T2"}),
    ("Marientor", "Rennweg", {"distance": 900, "mode": "tram", "line": "T2"}),
    ("Rennweg", "Doku-Zentrum", {"distance": 600, "mode": "tram", "line": "T2"}),
    ("Doku-Zentrum", "Dutzendteich", {"distance": 1100, "mode": "tram", "line": "T2"}),
    ("Dutzendteich", "Tiergärtnertor", {"distance": 800, "mode": "tram", "line": "T2"}),
    ("Plärrer", "Tiergärtnertor", {"distance": 1200, "mode": "tram", "line": "T3"}),
    ("Tiergärtnertor", "Dianaplatz", {"distance": 900, "mode": "tram", "line": "T3"}),
    ("Dianaplatz", "Veilhofstraße", {"distance": 800, "mode": "tram", "line": "T3"}),
    ("Veilhofstraße", "Thon", {"distance": 1000, "mode": "tram", "line": "T3"})
]
transport_graph.add_edges_from(tram_edges)

# Расстояния между станциями
distances = nx.get_edge_attributes(transport_graph, 'distance')

# Позиции вершин (станций метро и трамвайных линий)
pos = nx.get_node_attributes(transport_graph, 'pos')

# Цвета для веток метро і трамвайних линий
metro_colors = {"U1": "blue", "U2": "red", "U3": "green"}
tram_colors = {"T1": "orange", "T2": "purple", "T3": "brown"}

# Рисуем граф
plt.figure(figsize=(12, 12))

# Рисуем рёбра метро
for line, color in metro_colors.items():
    line_edges = [(u, v) for (u, v, d) in transport_graph.edges(data=True) if d["mode"] == "metro" and d["line"] == line]
    nx.draw_networkx_edges(transport_graph, pos, edgelist=line_edges, edge_color=color, width=2, label=line)

# Рисуем рёбра трамвайных линий
for line, color in tram_colors.items():
    line_edges = [(u, v) for (u, v, d) in transport_graph.edges(data=True) if d["mode"] == "tram" and d["line"] == line]
    nx.draw_networkx_edges(transport_graph, pos, edgelist=line_edges, edge_color=color, width=2, label=line)

# Рисуем узлы
nx.draw_networkx_nodes(transport_graph, pos, node_size=400, node_color="skyblue", edgecolors="black")

# Рисуем метки станций
nx.draw_networkx_labels(transport_graph, pos, font_size=10, font_weight="bold")

# Добавляем расстояния на рёбрах
nx.draw_networkx_edge_labels(transport_graph, pos, edge_labels=distances, font_color='red')

plt.title("Map of Nuremberg Metro and Tram Lines")
plt.axis('off')  # Отключаем оси координат
plt.legend()
plt.show()


# Тепер створимо графи для алгоритмів DFS і BFS

def get_path(graph, start, end, algorithm):
    if algorithm == "DFS":
        path = list(nx.dfs_edges(graph, source=start, depth_limit=20))  # Обмежуємо глибину
    elif algorithm == "BFS":
        path = list(nx.bfs_edges(graph, source=start))  # Використовуємо bfs_edges
    return [start] + [v for u, v in path]

# Знайдемо шляхи за допомогою обох алгоритмів
start_station = "Hauptbahnhof"
end_station = "Maffeiplatz"

dfs_path = get_path(transport_graph, start_station, end_station, "DFS")
bfs_path = get_path(transport_graph, start_station, end_station, "BFS")

print("DFS Path:", dfs_path)
print("BFS Path:", bfs_path)
