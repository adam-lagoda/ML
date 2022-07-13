import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    observation, reward, done, info = env.step(env.action_space.sample())
    print(observation, reward, done, info)
env.close()

#can use an atari or nintendo emulator with openai
#slide 53 lecture 3 (RL_Introduction) write custom environment