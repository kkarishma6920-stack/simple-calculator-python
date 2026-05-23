from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

print(Fore.CYAN + "=== Simple Calculator ===")

# User input
num1 = float(input(Fore.YELLOW + "Enter first number: "))
num2 = float(input(Fore.YELLOW + "Enter second number: "))

print(Fore.BLUE + "\nSelect Operation")
print(Fore.GREEN + "1. Addition")
print(Fore.GREEN + "2. Subtraction")
print(Fore.GREEN + "3. Multiplication")
print(Fore.GREEN + "4. Division")

choice = input(Fore.MAGENTA + "Enter choice (1/2/3/4): ")

# Operations
if choice == '1':
    result = num1 + num2
    print(Fore.CYAN + f"Result: {result}")

elif choice == '2':
    result = num1 - num2
    print(Fore.CYAN + f"Result: {result}")

elif choice == '3':
    result = num1 * num2
    print(Fore.CYAN + f"Result: {result}")

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(Fore.CYAN + f"Result: {result}")
    else:
        print(Fore.RED + "Error: Cannot divide by zero!")

else:
    print(Fore.RED + "Invalid input! Please select correct operation.")