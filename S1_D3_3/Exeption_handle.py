try:
    # x = int(input("Enter a number: "))
    result = 10 / 0
except ValueError as ve:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError as ze:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")
