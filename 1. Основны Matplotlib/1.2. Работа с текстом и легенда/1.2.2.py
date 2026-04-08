import matplotlib.pyplot as plt
import numpy as np

# Данные по курсу валют за месяц (30 дней)
days = np.arange(1, 31)

usd = [
    92.5,
    93.1,
    92.8,
    93.5,
    94.2,
    94.8,
    95.1,
    94.7,
    94.3,
    93.9,
    94.1,
    94.6,
    95.2,
    95.8,
    96.3,
    96.1,
    95.7,
    95.2,
    94.8,
    94.5,
    95.1,
    95.7,
    96.2,
    96.8,
    97.3,
    97.1,
    96.7,
    96.2,
    95.8,
    95.3,
]

eur = [
    99.8,
    100.2,
    100.5,
    100.1,
    101.3,
    102.1,
    102.5,
    102.3,
    101.8,
    101.2,
    101.5,
    102.0,
    102.8,
    103.5,
    104.1,
    103.9,
    103.4,
    102.9,
    102.4,
    102.1,
    102.7,
    103.3,
    103.9,
    104.6,
    105.2,
    105.0,
    104.5,
    104.0,
    103.5,
    102.9,
]

plt.plot(days, usd, label="USD", color="navy")
plt.plot(days, eur, label="EUR", color="green")
plt.xlabel("Дни месяца")
plt.ylabel("Курс (руб.)")
plt.title(
    "Динамика курсов валют: май 2026", fontsize="16", color="navy", fontweight="bold"
)
plt.annotate(
    "Макисимум USD",
    xy=(25, usd[25]),
    xytext=(23, 100),
    arrowprops=dict(facecolor="black", arrowstyle="->"),
)
plt.legend(loc="upper left")
plt.show()
