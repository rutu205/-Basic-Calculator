num1=float(input("Enter the first number:"))
op=input("Enter the operator:")
num2=float(input("Enter the second number:"))   
if op=='+':
   print(num1+num2)
elif op=='-':
   if num2 <= num1:
        print(num1 - num2)
   else:
      print("Cannot Subtract.The Second number is larger.")
   
elif op=='*':
   print(num1*num2)
elif op=='/':
   if num2!=0:
    print(num1/num2)
   else:
      print("Cannot divide.The second number is zero")
else:
    print("Operation invalid")