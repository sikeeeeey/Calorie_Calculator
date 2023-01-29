def add(x,y): 
    return x+y 

def sub(x, y): 
    return x-y

def mult(x,y): 
    return x*y

def div(x,y): 
    return x/y

def mod(x,y): 
    return  x%y

print("Enter: ")
print("1. For Addiiton")
print("2. For Substraction")
print("3. For Multiplication")
print("4. For Division")
print("5. For Modulus")

while True:
        
    choice = input("[1/2/3/4/5]: ")

    if choice in ['1','2','3','4','5']: 
        try: 
            num_1 = float(input("Enter the first number: "))
            num_2 = float(input("Enter the second number: "))
        except ValueError: 
            print("Invalid input. Please re-enter again!")
            continue

        if choice == '1': 
            print(num_1, "+", num_2, "=", add(num_1,num_2))

        elif choice == '2': 
            print(num_1, "-", num_2, "=", sub(num_1,num_2))

        elif choice == '3': 
            print(num_1, "x", num_2, "=", mult(num_1, num_2))

        elif choice == '4': 
            print(num_1, "/", num_2, "=", div(num_1,num_2))

        elif choice == '5': 
            print(num_1, "mod", num_2, "=", mod(num_1,num_2))

        next = input("Wanna give it another try? [y/n]: ")
        if next == "n": 
            break
    else: 
        print("Invalid output")

        