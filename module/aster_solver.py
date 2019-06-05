class Node(object):
    def __init__(self, state, start_point, goal_point):
        self.state = state
        self.start_point = start_point
        self.goal_point = goal_point
        self.hs = (self.state[0] - self.goal_point[0]) ** 2 + (self.state[1] - self.goal_point[1]) ** 2
        self.fs = 0
        self.parent_node = None
    
    def confirm_goal(self):
        if self.goal_point == self.state: return True
        else: return False

class NodeList(list):
    def find_nodelist(self, state):
        node_list = [t for t in self if t.state == state]
    def remove_from_nodelist(self, node):
        del self[self.index(node)]

class AsterSolver(object):
    def __init__(self, maze, start_point, goal_point):
        self.maze = maze
        self.start_point = start_point
        self.goal_point = goal_point
        self.open_list = NodeList()
        self.close_list = NodeList()
        self.trajectory = []
        self.shortest_route = []
    
    def set_initial_node(self):
        node = Node(self.start_point, self.start_point, self.goal_point)
        node.start_point = self.start_point
        node.goal_point = self.goal_point
        return node

    def __get_parent_node(self, node):
        self.shortest_route.append(node.state)
        if node.state[0] == self.start_point[0] and node.state[1] == self.start_point[1]:
            return node
        return self.__get_parent_node(node.parent_node)

    
    def go_next(self, next_actions, node):
        node_gs = node.fs - node.hs
        for action in next_actions:
            open_list = self.open_list.find_nodelist(node)
            dist = (node.state[0] - action[0]) ** 2 + (node.state[1] - action[1]) ** 2
            if open_list:
                if open_list.fs > node_gs + open_list.hs + dist:
                    open_list.fs = node_gs + open_list.hs + dist
                    open_list.parent_node = node
            else:
                open_list = self.close_list.find_nodelist(node)
                if open_list:
                    if open_list.fs > node_gs + open_list.hs + dist:
                        open_list.fs = node_gs + open_list.hs + dist
                        open_list.parent_node - node
                        self.open_list.append(open_list)
                        self.close_list.remove_from_nodelist(open_list)
                else:
                    open_list = Node(action, self.start_point, self.goal_point)
                    open_list.fs = node_gs + open_list.hs + dist
                    open_list.parent_node = node
                    self.open_list.append(open_list)

    def solve_maze(self):
        node = self.set_initial_node()
        node.fs = node.hs
        self.open_list.append(node)
        self.trajectory.append(node.state)

        while True:
            node = min(self.open_list, key = lambda node:node.fs)
            
            self.trajectory.append(node.state)
            if node.confirm_goal():
                self.close_list.append(node)
                self.__get_parent_node(self.close_list[-1])
                self.shortest_route.reverse()
                break

            self.open_list.remove_from_nodelist(node)
            self.close_list.append(node)

            next_actions = self.maze.get_actions(node.state)
            if self.trajectory[-2] in next_actions:
                del next_actions[next_actions.index(self.trajectory[-2])]
            self.go_next(next_actions, node)














