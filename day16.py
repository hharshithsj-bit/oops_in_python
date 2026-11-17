
# Day 16 - Exception Handling

print("===== EXCEPTION HANDLING =====")

# Example 1: Basic try and except
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
    print("Program execution completed.")


try:
    numbers = [10, 20, 30]
    index = int(input("\nEnter list index: "))

    print("Value:", numbers[index])

except IndexError:
    print("Error: Index is out of range!")

except ValueError:
    print("Error: Enter an integer!")



def check_age(age):
    if age < 18:
        raise ValueError("You are not eligible!")
    else:
        print("You are eligible!")

try:
    age = int(input("\nEnter your age: "))
    check_age(age)

except ValueError as e:
    print("Error:", e)


print("\n===== END OF DAY 16 =====")
