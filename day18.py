

print("===== EXCEPTION HANDLING =====")


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Division:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers!")

else:
    print("Division completed successfully!")

finally:
    print("Program execution finished.")



print("\n===== LIST EXAMPLE =====")

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter list index (0-4): "))
    print("Value:", numbers[index])

except IndexError:
    print("Error: Index is out of range!")

except ValueError:
    print("Please enter an integer!")



print("\n===== AGE CHECKING =====")

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("You must be 18 or older.")

    print("You are eligible!")

except ValueError as e:
    print("Error:", e)

print("\n===== END OF DAY 18 =====")
