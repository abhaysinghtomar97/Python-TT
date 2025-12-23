with open("C:\\Users\\Abhay Singh\\Workspace\\Training\\Python-TT\\File Handling\\2411085.jpg",'rb') as f1:
    data = f1.read()
    with open("C:\\Users\\Abhay Singh\\Workspace\\Training\\Python-TT\\File Handling\\a.jpg",'wb') as f2:
        f2.write(data)
