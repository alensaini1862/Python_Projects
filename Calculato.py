def add(x,y):
    sum = x+y
    return sum
def sub(x,y):
    sub = x - y
    return sub
def mul(x,y):
    mul = x*y
    return mul
def div(x,y):
    if y==0:
        return "cannot divid by zero"
    else:
     div= x/y
     return div
while True:
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '5':
        print("Exiting...")
        break

    x= float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(x, y))
    elif choice == '2':
        print("Result:", sub(x, y))
    elif choice == '3':
        print("Result:", mul(x, y))
    elif choice == '4':
        print("Result:", div(x, y))
    else:
        print("Invalid choice")

