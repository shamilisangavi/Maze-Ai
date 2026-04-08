from maze_env import MazeEnv
from q_agent import QAgent

env = MazeEnv()
agent = QAgent()

episodes = 200

for episode in range(episodes):

    state = env.reset()
    done = False

    while not done:

        action = agent.choose_action(state)

        next_state, reward, done = env.step(action)

        agent.update(state, action, reward, next_state)

        state = next_state


print("Training finished")


state = env.reset()
done = False

print("Agent solving maze:")

while not done:

    action = agent.choose_action(state)

    state, reward, done = env.step(action)

    print("State:", state)

print("Goal reached!")
