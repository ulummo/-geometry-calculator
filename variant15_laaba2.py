# Задача 1
year = int(input())
if 2001 <= year <= 2100:
    print("True")
else:
    print("False")

# Задача 2
number = int(input())
if (10 <= abs(number) <= 99) and (number % 2 == 0):
    print("True")
else:
    print("False")

# Задача 3
a = float(input())
b = float(input())
if a != 0:
    print(-b / a)
elif b == 0:
    print("inf")
else:
    print("no solution")
