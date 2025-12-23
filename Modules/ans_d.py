import pandas as pd
import numpy as np


df = pd.read_csv('students.csv')
students = df.values
marks = students[0:,2:]

average= np.mean(marks,axis=1)

for i in range(len(average)):
    print(students[i,1],":",average[i])
