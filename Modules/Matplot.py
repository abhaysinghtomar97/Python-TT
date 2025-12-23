import matplotlib.pyplot as plt

years = [2020, 2021, 2022, 2023, 2024]
values = [10, 20, 10, 40, 20]
plt.title("Sales Graph")
plt.xlabel("Years")
plt.ylabel("Profit")
plt.plot(years, values)
plt.show()
