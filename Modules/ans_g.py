import pandas as pd 
import matplotlib.pyplot as plt

data=pd.read_csv('cities.csv')

array = data.values

main_array = array[:,:-1]
min_array  = array[:,-1]

x=main_array[:,0]
y=main_array[:,1]

plt.figure(figsize=(6,4))
plt.plot(x, y, marker='o')
plt.xlabel('Cities')
plt.ylabel('Population in millions')
plt.title('City Populations')
plt.show()