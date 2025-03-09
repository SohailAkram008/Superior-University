class Node:
    def __init__(self, state, parent=None):
        self.state = state   
        self.parent = parent   
        self.g = 0   
        self.h = 0   
        self.f = 0   

    def __eq__(self, other):
        return self.state == other.state   

def a_star_search(start, goal, heuristic, graph):
    start_node = Node(start)
    goal_node = Node(goal)

    open_list = [start_node]   
    closed_list = []   

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        if current_node.state == goal_node.state:
            path = []
            total_cost = current_node.g
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1], total_cost   

        open_list.remove(current_node)
        closed_list.append(current_node)

        for neighbor_state, move_cost in graph.get(current_node.state, []):
            neighbor_node = Node(neighbor_state, current_node)

            if neighbor_node in closed_list:
                continue

            tentative_g_score = current_node.g + move_cost
            neighbor_node.h = heuristic(neighbor_state, goal)  
            neighbor_node.f = tentative_g_score + neighbor_node.h  

            if should_add_to_open(open_list, neighbor_node, tentative_g_score):
                neighbor_node.g = tentative_g_score
                open_list.append(neighbor_node)

    return None, None


def should_add_to_open(open_list, neighbor, new_g_score):
    for node in open_list:
        if neighbor == node and new_g_score >= node.g:
            return False  
    return True

def heuristic(state, goal):
    return 0  

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 5), ('E', 1)],
    'C': [('F', 3)],
    'D': [],
    'E': [('G', 2)],
    'F': [],
    'G': []
}

if __name__ == "__main__":
    start_state = 'A'
    goal_state = 'G'
    path, cost = a_star_search(start_state, goal_state, heuristic, graph)

    print("Optimal Path:", path)
    print("Total Cost:", cost)
