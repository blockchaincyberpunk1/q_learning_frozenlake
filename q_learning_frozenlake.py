import gym
import numpy as np

# Create the FrozenLake environment
env = gym.make("FrozenLake-v1")  # Use the appropriate environment ID

# Initialize the Q-table with zeros
num_states = env.observation_space.n
num_actions = env.action_space.n
Q = np.zeros((num_states, num_actions))

# Define Q-Learning parameters
learning_rate = 0.1
discount_factor = 0.99
num_episodes = 10000

# Loop through episodes for Q-Learning training
for episode in range(num_episodes):
    state = env.reset()  # Reset the environment for a new episode
    done = False

    while not done:
        # Choose an action using epsilon-greedy policy
        epsilon = 0.1
        if np.random.rand() < epsilon:
            action = env.action_space.sample()  # Explore: choose a random action
        else:
            action = np.argmax(Q[state, :])  # Exploit: choose the action with the highest Q-value

        # Perform the selected action
        new_state, reward, done, _ = env.step(action)

        # Update the Q-table using the Q-Learning equation
        Q[state, action] = (1 - learning_rate) * Q[state, action] + \
                           learning_rate * (reward + discount_factor * np.max(Q[new_state, :]))

        state = new_state  # Update the current state

    # Visualize the environment (optional)
    env.render()

# Print the learned Q-table
print("Learned Q-table:")
print(Q)

# Test the trained Q-table
total_rewards = 0
num_test_episodes = 100

for episode in range(num_test_episodes):
    state = env.reset()  # Reset the environment for a new test episode
    done = False

    while not done:
        action = np.argmax(Q[state, :])  # Use the learned policy (exploit): choose the action with the highest Q-value
        new_state, reward, done, _ = env.step(action)
        total_rewards += reward
        state = new_state  # Update the current state

# Calculate and print the average rewards over test episodes
average_reward = total_rewards / num_test_episodes
print(f"Average reward over {num_test_episodes} test episodes: {average_reward:.2f}")
