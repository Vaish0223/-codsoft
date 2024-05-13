num1 = float(input("Enter the first number:"))
opr = input("Enter the operator")
num2 = float(input("Enter the second number:"))

if(opr=="+"):
    print("The result is:",num1,"+",num2,"=",num1 + num2)
elif(opr=="-"):
    print("The result is:",num1,"+",num2,"=",num1 - num2)
elif(opr=="*"):
    print("The result is:",num1,"*",num2,"=",num1 * num2)
elif(opr=="/"):
    print("The result is:",num1,"/",num2,"=",num1 / num2)
elif(opr=="**"):
    print("The result is:",num1,"**",num2,"=",num1 ** num2)
elif(opr=="//"):
    print("The result is:",num1,"//",num2,"=",num1 // num2)
else:
    print("INVALID OPERATIONS, PLEASE PERFORM THE VALID OPERATION")