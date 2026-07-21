num1=int(input("Enter first number: "))
operator=input("Enter operator: + , - , * , / ")
num2=int(input("Enter second number: "))
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
  if num2==0:
    print("Invalid input")
  else:
    print(num1/num2)
else:
    print("Invalid operator")