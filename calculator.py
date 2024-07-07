print("\n")
print("-----WELCOME TO CALCULATOR PROGRAM -----")
print("\n")
def inputfun():
  n=int(input("Enter the no of values: "))
  inputs=[]
  for i in range(1,n+1):
    print("enter your",str(i)+ " value : ")
    b=int(input())
    inputs.append(b)
  return inputs

def addition():
  a=inputfun()  
  add=0
  for i in a:
    add+=i
  print("Added value is ",add)

def subtraction():
  a=inputfun()
  sub=a[0]
  for i in range(1,len(a)):
    sub-=a[i]
  print("Subtracted value is",sub)

def multiplication():
  a=inputfun()
  mul=1
  for i in a:
    mul*=i
  print("Multiplied value is",mul)

def division():
  a=inputfun()
  div=a[0]
  for i in range(1,len(a)):
    div/=a[i]
  print("Divided value is",div)

def floordivision():
  a=inputfun()
  floordiv=a[0]
  for i in range(1,len(a)):
    floordiv//=a[i]
  print("Floor Division value is",floordiv)

def modulus():
  print("1.Modulo")
  print("2.Addition modulo")
  print("3.multiplication modulo")
  choice2=int(input("Enter your choice: "))
  if choice2==1:
    a=int(input("Enter the first value: "))
    b=int(input("Enter the second value: "))
    print("The result is:",a%b)
  if choice2==2:
    inputs=[]
    n=int(input("Enter the no of values for addition: "))
    for i in range(1,n+1):
      print("enter your",str(i)+ " value : ")
      b=int(input())
      inputs.append(b)
    addmodulo=int(input("Enter your value for modulus: "))      
    add=0
    for i in inputs:
      add+=i
    print("Result is ",add%addmodulo)
  elif choice2==3:
    inputs=[]
    n=int(input("Enter the no of values for Multiplication: "))
    for i in range(1,n+1):
      print("enter your",str(i)+ " value : ")
      b=int(input())
      inputs.append(b)
    mulmodulo=int(input("Enter your value for modulus: "))      
    mul=1
    for i in inputs:
      mul*=i
    print("Result is ",mul%mulmodulo)    
  
def exponential():
  a=int(input("Enter the base value: "))
  b=int(input("Enter the power value: "))
  print("The result value is",a**b)
def squareroot():
  a=int(input("Enter the value: "))
  print("The result value is",a**0.5)
def percentage():
  a=int(input("Enter the value: "))
  print("Result is",a/100)

while True:
  print("\n")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Floor Division")
  print("6. Modulus")
  print("7. Exponential")
  print("8. Square Root")
  print("9. Percentage")
  print("10. TYPE END TO CLOSE THE CALCULATOR  ")
  print("\n")
  print("Enter your choice: ")
  choice=input().upper()
  if choice=="1":
    addition()
  elif choice=="2":
    subtraction()
  elif choice=="3":
    multiplication()
  elif choice=="4":
    division()
  elif choice=="5":
    floordivision()
  elif choice=="6":
    modulus()
  elif choice=="7":
    exponential()
  elif choice=="8":
    squareroot()
  elif choice=="9":
    percentage()
  elif choice=="END":
    break

else:
   print("enter your choice correctly")



