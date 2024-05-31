from queue import PriorityQueue

# En uzun mesafeyi hesaplayan yardımcı fonksiyon
def longest_edge(path, distances):
    max_distance = 0
    for i in range(len(path) - 1):
        max_distance = max(max_distance, distances[path[i]][path[i + 1]])
    return max_distance

# Heuristic fonksiyonu
def heuristic(state, cities, distances):
    remaining_cities = [city for city in cities if city not in state]
    if not remaining_cities:
        return 0
    current_city = state[-1]
    return max(distances[current_city][city] for city in remaining_cities)

# TSP problemi için basit bir sınıf
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
        return len(state) == len(self.cities) + 1 and state[-1] == self.initial

    def path_cost(self, path):
        return longest_edge(path, self.distances)

# A* Search algoritması
def astar_search(problem):
    initial_state = (problem.initial,)
    initial_heuristic = heuristic(initial_state, problem.cities, problem.distances)
    frontier = PriorityQueue()
    frontier.put((initial_heuristic, initial_state))
    explored = set()

    while not frontier.empty():
        _, state = frontier.get()

        if problem.goal_test(state):
            return state

        explored.add(state)

        for action in problem.actions(state):
            child_state = problem.result(state, action)
            if child_state not in explored:
                cost = longest_edge(child_state, problem.distances)
                h = heuristic(child_state, problem.cities, problem.distances)
                frontier.put((cost + h, child_state))

    return None

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
    solution = astar_search(problem)
    print("A* Search Çözümü:", solution)