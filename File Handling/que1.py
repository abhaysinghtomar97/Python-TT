import csv

with open("C:\\Users\\Abhay Singh\\Workspace\\Training\\Python-TT\\File Handling\\products.csv",'r') as f1:
    data = csv.reader(f1)
    threshold = '200'
    for i in data:
        if i[5]<threshold:
            print(i)

