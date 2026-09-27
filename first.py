print("select operation from the given list \n 1.addition \n 2.substraction \n 3.multiplication \n 4.division \n 5. mean")
oper = input("please enter number of the following operation to execute :")

var1 = float(input("please enter first number :"))
var2 = float(input("please enter second number :"))

def calculate(a,b,oper):
    if oper == "1" : 
        return a+b        
    elif oper == "2":
        return a-b        
    elif oper == "3":
        return a*b
    elif oper == "4":
        return a/b
    elif oper == "5":
        return (a+b)/2   
    else:   
        print("select valid action!")


def get_oper_name(oper):
     if oper == "1" : 
         return "addition"
        
     elif oper == "2":
         return "substraction"
        
     elif oper == "3":
         return "multiplication"
        
     elif oper == "4":
         return "divide"
        
     elif oper == "5":
         return "average"       
     else:   
         return "invalid operation!"

print(f"the {get_oper_name(oper)} of {var1} and {var2} is {calculate(var1,var2,oper)}")



# if oper == "1" :
#     print(f"the sum of {var1} and {var2} is {add2num(var1,var2)}")
# elif oper == "2":
#     print(f"the diffrence between {var1} and {var2} is {sub2num(var1,var2)}")
# elif oper == "3":
#     print(f"the multiplication of {var1} and {var2} is {multi2num(var1,var2)}")
# elif oper == "4":
#     print(f"if {var1} divided by {var2}, the result is {divide2num(var1,var2)}")
# else:
#     print(f"invalid operation has been selected !")    

# def add2num(a,b):   
#     return a+b
    
# def sub2num(a,b):
#     return a-b

# def multi2num(a,b):
#     return a*b

# def divide2num(a,b):
#     return a/b

    
 