for row in range(6):  
    for col in range(7):  
        if (row==0 and col %3 !=0)or(row==1 and col %3==0) or(row-col==2) or(row+col==8):  
            print(u"\u2661",end=" ")  
        else:  
            print(end=" ")  
    print() 
print(  "THIS is the love calculator software wich calculate your love percentage")

name = input("Enter your name ?")
name2 = input("Enter the name of the person With you want to check youur love percentage?Tero chamma ko nam vannn")

if name == "samir" and name2 == "mia":
    print(f"The love percentage of {name} and {name2} is 100 percentage")
else:
    import random
    per = random.randint(1,101)
    print(f"The love percentage of {name} and {name2} is {per} percentage")
for row in range(6):  
    for col in range(7):  
        if (row==0 and col %3 !=0)or(row==1 and col %3==0) or(row-col==2) or(row+col==8):  
            print(u"\u2661",end=" ")  
        else:  
            print(end=" ")  
    print()
