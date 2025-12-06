print("Welcome to calculator choose numbers 1-4")
print("1 = add")
print("2 = subtract")
print("3 = multiply")
print("4 = divide")
user=(int(input("enter numbers 1-4: ")))

if user==1:
    first=int(input("Enter first number: "))
    second=int(input("Enter second number: "))
    sum=first+second 
    print("answer = ",sum)
elif user==2:
    first=int(input("Enter first number: "))
    second=int(input("Enter second number: "))
    sum=first-second
    print("answer = ",sum)
elif user==3:
    first=int(input("Enter first number: "))
    second=int(input("Enter second number: "))
    sum=first*second
    print("answer = ",sum)
elif user==4:
    first=int(input("Enter first number: "))
    second=int(input("Enter second number: "))
    sum=first/second
    print("answer = ",sum)
else:
    print("not a valid choice pick again!")