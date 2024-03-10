print("Simple Calculator Application")


while True:
    print("----------------------------")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Exit")
    choice = input("\nEnter your choice: ")
    
    if(choice == "1"):
        a = int(input("Enter the number of a: "))
        b = int(input("Enter the number of b: "))
        result = a+b
        print("The addition of", a,"+",b ,"=", result)
    elif(choice == "2"):
        a = int(input("Enter the number of a: "))
        b = int(input("Enter the number of b: "))
        result = a-b
        print("The subtraction of", a,"-",b ,"=", result)
    elif(choice == "3"):
        a = int(input("Enter the number of a: "))
        b = int(input("Enter the number of b: "))
        result = a*b
        print("The multiplication of",a,"*",b ,"=", result)
    elif(choice == "4"):
        a = int(input("Enter the number of a: "))
        b = int(input("Enter the number of b: "))
        result = a/b
        print("The divison of", a,"/",b , "=", result)
    elif(choice == "5"):
         break
    else:
        print("Invalid Choice")
        

