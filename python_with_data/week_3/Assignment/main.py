import calculation
import result

while True:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("1. Add\n2. Subtract\n3. Divide\n4. Exit")
    choice = int(input("Choose operation (1-4): "))

    if choice == 1:
        res = calculation.add(num1, num2)
        result.show_result(num1, num2, "Addition", res)

    elif choice == 2:
        res = calculation.subtract(num1, num2)
        result.show_result(num1, num2, "Subtraction", res)

    elif choice == 3:
        res = calculation.divide(num1, num2)
        result.show_result(num1, num2, "Division", res)

    elif choice == 4:
        print("Calculator closed.")
        break

    else:
        print("Invalid choice!")