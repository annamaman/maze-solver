class Maze(object):
	def __init__(self, maze, start_point, goal_point):
		self.maze = maze
		self.start_point = start_point
		self.goal_point = goal_point
		self.movable_vec = [[1,0], [-1,0], [0,1], [0,-1]]
	
	def display(self):
		print("start : " + str(self.start_point) + "  goal : " + str(self.goal_point))
		for line in self.maze:
			print(line)

	def get_actions(self, state):
		movables = []
		for vec in self.movable_vec:
			next_state = [state[0] + vec[0], state[1] + vec[1]]
			if next_state[0] < 0 or next_state[0] >= len(self.maze) or next_state[1] < 0 or next_state[1] >= len(self.maze):
				continue
			if self.maze[next_state[0]][next_state[1]] == "S":
				movables.append(next_state)
		return movables