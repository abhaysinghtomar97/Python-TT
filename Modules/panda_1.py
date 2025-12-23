import pandas as pd


data = {
    "Food": [
        "Meat", "Banana", "Avocados", "Sweet-Potatoes", "Spinach",
        "Watermelon", "Coconut-water", "Beans", "Legumes", "Tomato"
    ],
    "Calories": [250, 130, 140, 120, 20, 20, 10, 50, 40, 19],
    "Potassium": [40, 55, 20, 30, 40, 32, 10, 26, 25, 20],
    "Fat": [8, 5, 3, 6, 1, 1.5, 0, 2, 1.5, 2.5]
}

df=pd.DataFrame(data)
# df.to_csv('Mynewdata.csv')
a = pd.read_csv('Mynewdata.csv')

print(a)