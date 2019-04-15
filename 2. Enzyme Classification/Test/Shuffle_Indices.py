import numpy as np

indices = np.random.permutation(range(n_total))[:n_total]
y_input = y[indices]
x_input = x[indices]