str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")
set1= set()
for i in str1:
    for j in str2:
        if(i==j):
            set1.add(i)
            
for i in set1:
    print(i)   