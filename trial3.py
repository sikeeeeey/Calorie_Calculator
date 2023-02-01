orange_calorie = 0.47
chicken_breast = 1.65

def orange(x): 
    return orange_calorie*x

print("Choose a food: ")
print("1. For Orange")
print("2. For Chicken Breast")

while True: 

    choice = input("[1/2]: ")

    try: 
        weight = float(input("Enter the weight of your food: "))

    except ValueError: 
        print("Input Error")

    if choice in ['1', '2']: 

        if choice == '1': 
            print("Total calories are: ", orange(weight))

        elif choice == '2': 
            print("Total calories are: ", chicken_breast(weight))

        next = input("Calculate again? [y/n]: ")
        if next == "n": 
            break

    else: 
        print("Wrong Output")