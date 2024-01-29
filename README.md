# FrozenLake Q-Learning

![FrozenLake Q-Learning](frozenlake.jpg)

FrozenLake Q-Learning is a Python project that uses the OpenAI Gym library to implement a Q-Learning algorithm for solving the FrozenLake environment. This project demonstrates how to train an agent to navigate a frozen lake and reach the goal using Q-Learning.

## Overview

The FrozenLake environment is a grid world where an agent starts at a specific position and needs to reach a goal while avoiding holes in the ice. Q-Learning is a reinforcement learning technique used to find the optimal action for each state in such an environment.

In this project, we use Q-Learning to train an agent to make decisions based on maximizing its expected future rewards. The Q-table is used to store the estimated values (Q-values) for each state-action pair. Over time, the agent learns the best actions to take in each state to achieve its goal.

## Project Structure

- `q_learning_frozenlake.py`: The main Python script that implements the Q-Learning algorithm.
- `frozenlake.jpg`: An image representing the FrozenLake environment (optional).
- `README.md`: This README file.

## Dependencies

- gym: The OpenAI Gym library for creating and managing reinforcement learning environments.
- numpy: A library for numerical operations, used for Q-table manipulation.

## Usage

1. Make sure you have Python, gym, and numpy installed on your system.
2. Run the `q_learning_frozenlake.py` script to start training the agent using Q-Learning.
3. The agent will explore and learn the optimal policy to navigate the FrozenLake environment.
4. After training, the learned Q-table will be displayed, showing the Q-values for each state-action pair.
5. The agent's performance will be tested in the environment, and the average reward over multiple test episodes will be displayed.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Author

- Sheneeza Volcov

Feel free to contribute to this project or use it as a learning resource for Q-Learning in reinforcement learning.
