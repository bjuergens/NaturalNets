import json
import time
import os
from brains.continuous_time_rnn import *
from environments.collect_points import *

directory = os.path.join('Simulation_Results', '2021-03-20_11-07-09')

# Load configuration file
with open(os.path.join(directory, 'Configuration.json'), "r") as read_file:
    configuration = json.load(read_file)

brain_state = ContinuousTimeRNN.load_brain_state(os.path.join(directory, 'Brain_State.npz'))

individual = np.load(os.path.join(directory, 'Best_Genome.npy'), allow_pickle=True)

brain = ContinuousTimeRNN(input_size=0, output_size=0, individual=individual, configuration=configuration['brain'],
                          brain_state=brain_state)

number_validation_runs = configuration['number_validation_runs']

fitness_total = 0

for env_seed in range(number_validation_runs):

    env = CollectPointsEnv(env_seed=env_seed, configuration=configuration['environment'])

    ob = env.reset()
    brain.reset()

    fitness_current = 0
    done = False

    while not done:
        action = brain.step(ob)
        ob, rew, done, info = env.step(action)
        fitness_current += rew

        env.render()
        time.sleep(0.005)

    fitness_total += fitness_current

    print("Seed: {}   Reward:  {:4.2f}".format(env_seed, fitness_current))

print("Reward mean: {:4.2f}".format(fitness_total / number_validation_runs))
print("Finished")
