def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"The PGCD of {a} and {b} is {pgcd(a, b)}")

