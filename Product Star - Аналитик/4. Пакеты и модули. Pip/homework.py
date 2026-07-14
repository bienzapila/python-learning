import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])

data = {'Дни': x, 'Продуктивность, %': [50, 70, 60, 90, 100]}
df = pd.DataFrame(data)

print(df)

plt.plot(df['Дни'], df['Продуктивность, %'])
plt.show()