import gym
import rm_gym
import time

if __name__ == '__main__':
    env = gym.make("RoboMaster-v0")
    env.reset()
    while True:
        for i in range(4):
            env.render()
            env.step([20,0,0,0], 0)
            env.step([-20, 0, 0, 0], 1)
            env.step([20, 0, 0, 0], 2)
            env.step([-20, 0, 0, 0], 3)
            time.sleep(0.1)