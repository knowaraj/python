#Weekdays Using match case
x=input("Enter Your Day Number : ")
x=int(x)
match x:
    case 1: 
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Enter corect choice 1-7.")
    
    