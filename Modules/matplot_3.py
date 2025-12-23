# question f

import matplotlib.pyplot as plt

food=[
        "Meat", "Banana", "Avocados", "Sweet-Potatoes", "Spinach",
        "Watermelon", "Coconut-water", "Beans", "Legumes", "Tomato"
    ]
Calories= [250, 130, 140, 120, 20, 20, 10, 50, 40, 19]
Potassium= [40, 55, 20, 30, 40, 32, 10, 26, 25, 20]
Fat = [8, 5, 3, 6, 1, 1.5, 0, 2, 1.5, 2.5]


x = list(range(len(food)))
width = 0.25
plt.figure()

plt.bar([i-width for i in x],Calories,width, label='Calories')
plt.bar(x,Potassium,width, label='Potassium')
plt.bar([i+width for i in x],Fat,width, label='Fat')
plt.xticks(x,food,rotation=45)

plt.xlabel('Foods')
plt.ylabel("Nutritional Values")

plt.legend()
plt.show()