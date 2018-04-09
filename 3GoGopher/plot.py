import numpy as np
# import matplotlib.pyplot as plt
#
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
#
# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii
#
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

N = 1000
df = pd.read_csv("data.csv")
colors = np.random.rand(N)
df.plot(kind='scatter', x='x', y='y', alpha=0.2)  # scatter plot
plt.show()

print('ok')

import time

while True:
    time.sleep(1)
