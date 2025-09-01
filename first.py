N = int(input("enter the number: "))
a = N % 10
N = N // 10
b = N % 10
N = N // 10
c = N % 10
sum = a + b + c
print("Sum of digits:", sum)