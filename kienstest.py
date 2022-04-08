import matplotlib.pyplot as plt
import numpy as np

# We define two sequences x, y as numpy array
# where y is actually a sub-sequence from x
# x = np.array([0,0,0.5,2,0,1,0]).reshape(-1, 1)
x = np.array([0,0,0,1,0,10]).reshape(-1, 1)
y = np.array([0,2,0,1,0,0]).reshape(-1, 1)

plt.plot(x, label='x')
plt.plot(y, label='y')
plt.title('Our two temporal sequences')
plt.legend()

from dtw import dtw

# Here, we use L2 norm as the element comparison distance
l2_norm = lambda x, y: np.abs(x-y)

dist, cost_matrix, acc_cost_matrix, path = dtw(x, y, dist=l2_norm)

print(dist)

# plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
# plt.plot(path[0], path[1], 'w')
plt.show()