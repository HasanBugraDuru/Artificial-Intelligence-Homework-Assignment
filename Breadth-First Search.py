from queue import Queue

# Şehirler arası mesafeleri hesaplayan yardımcı fonksiyon
def longest_edge(path, distances):
    max_distance = 0
    for i in range(len(path) - 1):
        max_distance = max(max_distance, distances[path[i]][path[i + 1]])
    return max_distance

# TSP problem tanımı
class TSPProblem:
    def __init__(self, cities, distances):
        self.cities = cities
        self.distances = distances
        self.initial = cities[0]

    def actions(self, state):
        return [city for city in self.cities if city not in state]

    def result(self, state, action):
        return state + (action,)

    def goal_test(self, state):
        return len(state) == len(self.cities) and state[-1] == self.initial

    def path_cost(self, path):
        return longest_edge(path, self.distances)

# BFS algoritması
def bfs(problem):
    initial_state = (problem.initial,)
    frontier = Queue()
    frontier.put((initial_state, 0))  # (state, path_cost)
    explored = set()

    best_path = None
    best_cost = float('inf')

    while not frontier.empty():
        state, path_cost = frontier.get()

        if problem.goal_test(state):
            current_cost = problem.path_cost(state)
            if current_cost < best_cost:
                best_path = state
                best_cost = current_cost
            continue

        explored.add(state)

        for action in problem.actions(state):
            child_state = problem.result(state, action)
            if child_state not in explored:
                next_cost = max(path_cost, problem.distances[state[-1]][action])
                frontier.put((child_state, next_cost))

    return best_path

# Örnek kullanım
if __name__ == "__main__":
    cities = ['A', 'B', 'C', 'D']
    distances = {
        'A': {'A': 0, 'B': 2, 'C': 9, 'D': 10},
        'B': {'A': 1, 'B': 0, 'C': 6, 'D': 4},
        'C': {'A': 15, 'B': 7, 'C': 0, 'D': 8},
        'D': {'A': 6, 'B': 3, 'C': 12, 'D': 0}
    }

    problem = TSPProblem(cities, distances)
    solution = bfs(problem)
    print("BFS Çözümü:", solution)