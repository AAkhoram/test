n=int(input("Enter a number: "))
a=n%5
b=n%3
c=n%2
if a==0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")
if b==0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")
if c==0:
    print("The number is divisible by 2")
else:
    print("The number is not divisible by 2")
