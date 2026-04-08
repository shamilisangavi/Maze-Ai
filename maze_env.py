import numpy as np

class MazeEnv:

    def __init__(self):

        self.maze = np.array([
            [0,0,0,1],
            [1,0,0,1],
            [0,0,0,0],
            [1,1,0,2]
        ])

        self.start = (0,0)
        self.goal = (3,3)
        self.agent_pos = self.start


    def reset(self):

        self.agent_pos = self.start
        return self.state()


    def state(self):

        return self.agent_pos


    def step(self, action):

        x,y = self.agent_pos

        if action == 0:  # up
            x -= 1
        elif action == 1:  # down
            x += 1
        elif action == 2:  # left
            y -= 1
        elif action == 3:  # right
            y += 1


        if x < 0 or y < 0 or x >= 4 or y >= 4:
            return self.state(), -1, False

        if self.maze[x][y] == 1:
            return self.state(), -1, False


        self.agent_pos = (x,y)

        if self.maze[x][y] == 2:
            return self.state(), 10, True


        return self.state(), -0.1, False
