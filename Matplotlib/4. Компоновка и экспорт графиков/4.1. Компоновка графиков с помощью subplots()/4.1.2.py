import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Загрузка данных
iris = load_iris()
data = iris.data
target = iris.target
target_names = iris.target_names
feature_names = iris.feature_names

# Извлечение признаков
sepal_length = data[:, 0]  # длина чашелистика
sepal_width = data[:, 1]   # ширина чашелистика
petal_length = data[:, 2]  # длина лепестка
petal_width = data[:, 3]   # ширина лепестка

print("Названия признаков:", feature_names)
print("Названия классов:", target_names)
print("Количество образцов:", data.shape[0])

fig, axes = plt.subplots(2, 2)
target = iris.target
target_names = iris.target_names

unique, counts = np.unique(target, return_counts=True)
print(f"Виды: {target_names}")
print(f"Количество: {counts}")

axes[0, 0].pie(counts, labels=target_names, autopct='%1.1f%%')
axes[0, 0].set_title('Распределение видов ирисов')


axes[0, 1].hist(sepal_length, bins=25, alpha=0.7)
axes[0, 1].set_xlabel('Частота')
axes[0, 1].set_ylabel('Длина чашелистника')
axes[0, 1].set_title('Распределение длины чашелистника у ирисов')


axes[1, 1].scatter(petal_width, petal_length)

sepal_length_setosa = sepal_length[target == 0]      # вид setosa (индекс 0)
sepal_length_versicolor = sepal_length[target == 1]  # вид versicolor (индекс 1)
sepal_length_virginica = sepal_length[target == 2]   # вид virginica (индекс 2)
axes[1, 0].boxplot([sepal_length_setosa, sepal_length_versicolor, sepal_length_virginica])

plt.show()