#WAP to college management system having atleast 8-9 functions/ moduels , you should use functions of following types: 
#1) Funciton with arg
#2) Funciton without arg
#3) Funciton with return type
#4) Funciton without return types  
#5) Funciton with kwargs(key-value pairs)

def marks(s_name):
    phy = int(input("Enter Physics marks: "))
    chem = int(input("Enter chemistry marks: "))
    math = int(input("Enter Maths marks: "))
    print(s_name, "Percentage is: ", (phy+phy+math)/3)
    
def attendence():
    attended = int(input("Enter lectures attended: "))
    total = int(input("Enter total lectures: "))
    return (attended/total)*100

def student_count():
    total_sec = int(input("Enter total Number Branches: "))
    student_sec = int(input("Enter Student in each Branche: "))

    return total_sec * student_sec




s_name = input("Enter student Name: ")
s_brach = input("Enter Branach: ")


