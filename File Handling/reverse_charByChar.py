with open("C:\\Users\\Abhay Singh\\Workspace\\Training\\Python-TT\\File Handling\\reverse_charByChar.txt",'r') as f1:
    f2 = f1.read()

    reversed = f2[ : :-1]
  
    for i in reversed:
        print(i, end=",")