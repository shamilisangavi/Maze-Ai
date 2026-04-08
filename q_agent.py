import numpy as np
import random

class QAgent:

    def __init__(self):

        self.q_table = np.zeros((4,4,4))

        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.2


    def choose_action(self, state):

        x,y = state

        if random.random() < self.epsilon:
            return random.randint(0,3)

        return np.argmax(self.q_table[x][y])


    def update(self, state, action, reward, next_state):

        x,y = state
        nx,ny = next_state

        best_next = np.max(self.q_table[nx][ny])

        old = self.q_table[x][y][action]

        self.q_table[x][y][action] = old + self.alpha * (
            reward + self.gamma * best_next - old
        )
