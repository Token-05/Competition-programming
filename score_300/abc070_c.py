import numpy as np

N = int(input())
T = np.array(list(int(input()) for i in range(N)))
print(np.lcm.reduce(T))