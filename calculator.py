a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
print("Choose operation:")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
choice=input("ENter your choice:")
if choice=='1':
  print("a+b:",a+b)
elif choice=='2':
  print("a-b:",a-b)
elif choice=='3':
  print("a*b:",a*b)
elif choice=='4':
  if b!=0:
    print("a/b:",a/b)
  else:
    print("Cannot divide by zero")
else:
  print("Invalid choice")

