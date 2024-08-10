#command-line calculator application to perform basic arithmetic operations.
#by Lucky Ali
#Date: 2024-08-10

#function to add
def add(x, y):
    return x + y

#function to subtract
def subtract(x, y):
    return x - y

#function to multipy
def multiply(x, y):
    return x * y

#function to divide
def divide(x, y):
    if y == 0:
        return "Error: Division by zero."
    return x / y

#main function to get user input and perform operations
def main():
    #using loop to allow continuous calculations until the user decides to exit
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator.")
            break

        #ensuring the operator selection is valid
        if choice in ['1', '2', '3', '4']:
            #checking if input is indeed a number
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
        else:
            print("Error: Invalid Input")

#checks if the script is being run directly
if __name__ == "__main__":
    main()
