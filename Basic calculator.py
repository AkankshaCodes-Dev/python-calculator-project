#basic calculator
print("Basic calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
while True:
    #asking inputs from user
    choice = int(input("Enter choice(1/2/3/4):"))
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    #performing operations based on user input
    if choice == 1:
        result = num1 + num2
        print(f"Result:{num1} + {num2} = {result}")
    elif choice == 2:
        result = num1 - num2
        print(f"Result:{num1} - {num2} = {result}")
    elif choice == 3:
         result = num1 * num2
         print(f"Result:{num1} * {num2} = {result}")
    elif choice == 4:
         if num2 != 0:
              result = num1 / num2
              print(f"Result:{num1} / {num2} = {result}")            
         else:
              print("Cannot divide by zero.")
    else:
         print("Invalid choice!please choose 1, 2, 3 or 4.")     
     #asking user to continue or stop
    select = input("Do you want to continue?(yes/no):").lower()
    if select == "no":
         break

        
