from queue import PriorityQueue

# En uzun mesafeyi hesaplayan yardımcı fonksiyon
def longest_edge(path, distances):
    max_distance = 0
    for i in range(len(path) - 1):
        max_distance = max(max_distance, distances[path[i]][path[i + 1]])
    return max_distance

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

# Uniform Cost Search algoritması
def uniform_cost_search(problem):
    initial_state = (problem.initial,)
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    explored = set()

    while not frontier.empty():
        cost, state = frontier.get()

        if problem.goal_test(state):
            return state

        explored.add(state)

        for action in problem.actions(state):
            child_state = problem.result(state, action)
            if child_state not in explored:
                new_cost = max(cost, problem.distances[state[-1]][action])
                frontier.put((new_cost, child_state))

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
    solution = uniform_cost_search(problem)
    print("Uniform Cost Search Çözümü:", solution)