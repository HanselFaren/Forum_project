import math
n = int(input("Enter a numerator: Value must be greater than 0: "))
while True:
    if n <= 0:
        n = int(input("Please re-enter the numerator. Value must be greater than 0: "))
    else:
        break
d = int(input("Enter a denominator. Value must be greater than 0: "))
while True:
    if d <= 0:
        d = int(input("Please re-enter the denominator. Value must be greater than 0: "))
    else:
        break

g = math.gcd(n,d)
n1 = n // g
d1 = d // g
m = n1 % d1
w = n1 // d1
if n < d:
    print(f"{n}/{d} is a proper fraction.")
    if g != 1:
        print(f"This proper fraction can be reduced to: {n1}/{d1}")
    else:
        print("This proper fraction cannot be reduced any further.")
elif n > d:
    print(f"{n}/{d} is an improper fraction.")
    if  g == 1:
        print("This improper fraction cannot be reduced any further.")
        if m == 0:
            print(f"The whole number is {w}")
        else:
            print(f"The mixed number is {w} and {m}/{d1}")
    else:
        print(f"This improper fraction can be reduced to: {n1}/{d1}")
        if m == 0:
            print(f"The whole number is {w}")
        else:
            print(f"The mixed number is {w} and {m}/{d1}")