from itertools import combinations

# Для чтения файла будет две вспомогательные функции. 
# Следующая - переделывает одну конкретную текстовую матрицу в матрицу смежности в виде массива
def read_one_graph_from_text(text):
    adjacency_matrix = []
    lines = text.strip().split('\n')
    for line in lines:
        row = [int(char) for char in line.strip()]
        adjacency_matrix.append(row)
    return adjacency_matrix

# Эта - выделяет среди всего файла текстовые матрицы смежности
def read_all_graphs_from_file(file_path):
    graphs = []
    with open(file_path, 'r') as file:
        file_content = file.read()
        graph_texts = file_content.strip().split('\n\n')
        for graph_text in graph_texts:
            graphs.append(read_one_graph_from_text(graph_text))

    return graphs

# Укажите здесь абсолютный путь к файлу txt
file_path = "/bla/bla/bla/bla/bla.txt"

# Эта функция вернет нам матрицы смежности всех графов
graphs = read_all_graphs_from_file(file_path)

def ContainsAntitriangle(graph):
    for a, b, c in combinations(list(range(7)), 3):
        if (graph[a][b] == 0) and (graph[b][c] == 0) and (graph[c][a] == 0):
            return True
    return False

def ContainsC4(graph):
    for a, b, c, d in combinations(list(range(7)), 4):
        if ((graph[a][b] == 1) and (graph[b][c] == 1) and (graph[c][d] == 1) and (graph[d][a] == 1) or
            (graph[a][c] == 1) and (graph[b][d] == 1) and (graph[a][d] == 1) and (graph[b][c] == 1) or 
            (graph[a][b] == 1) and (graph[a][c] == 1) and (graph[d][b] == 1) and (graph[d][c] == 1)):
            return True
    return False

counter = 0

for graph in graphs:
    if not ContainsC4(graph) and not ContainsAntitriangle(graph):
        counter += 1
print(counter)
