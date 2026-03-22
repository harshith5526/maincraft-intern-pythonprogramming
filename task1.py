print("1. Sum of Two Numbers")
print("2. Odd or Even")
print("3. Factorial")
print("4. Fibonacci")
print("5. String Reverse")
print("6. Palindrome Check")
print("7. Leap Year")
print("8. Armstrong Number")

choice = int(input("Enter your choice (1-8): "))

# 1. Sum
if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum =", a + b)

# 2. Odd or Even
elif choice==2:
    num=int(input("Enter number: "))
    if num %2==0:
        print("Even")
    else:
        print("Odd")

# 3. Factorial
elif choice==3:
    n=int(input("Enter number: "))
    fact=1
    for i in range(1, n+1):
        fact=fact*i
    print("Factorial =", fact)

# 4. Fibonacci
elif choice==4:
    n=int(input("Enter n: "))
    a,b=0,1
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c


# 5. String Reverse
elif choice==5:
    s=input("Enter string: ")
    rev=""
    for i in s:
        rev=i+rev
    print("Reversed string:",rev)

# 6. Palindrome
elif choice==6:
    word=input("Enter string: ")
    rev=""
    for i in word:
        rev=i+rev
    if word==rev:
        print("Palindrome")
    else:
        print("Not a palindrome")

# 7. Leap Year
elif choice==7:
    year=int(input("Enter year: "))
    if (year%4==0 and year%100!=0) or (year%400==0):
        print("Leap Year")
    else:
        print("Not Leap Year")

# 8. Armstrong Number
elif choice==8:
    n=int(input("Enter number: "))
    temp=n
    power=len(str(n))
    total=0

    while temp>0:
        digit=temp%10
        total=total+(digit**power)
        temp=temp//10

    if total==n:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

else:
    print("Invalid choice")