try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(a + b)
except ValueError:
    print("Please enter valid numeric inputs.")
