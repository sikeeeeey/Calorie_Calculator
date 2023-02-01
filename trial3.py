orange_calorie = 0.47
orange_protein = 0.009

chicken_breast_calorie = 1.65
chicken_breast_protein = 0.31

chicken_liver_calorie = 1.67
chicken_liver_protein = 0.24


sugar_calorie= 3.87 
sugar_prortein = 0.00

lentils_calorie = 3.44
lentils_protein = 0.26

carrot_calorie = 0.41
carrot_protein = 0.09

milk_calorie = 0.67
milk_protein = 0.033

potato_calorie = 0.77
potato_protein = 0.02

curd_calorie = 0.98
curd_protein = 0.10

goat_blood_calorie = 80
goat_blood_protein = 0.21

def orange(x): 
    return orange_calorie*x

def orange_protein_fun(x):
    return orange_protein*x 

def chicken_breast(x): 
    return chicken_breast_calorie*x

def chicken_liver(x): 
    return chicken_liver_calorie*x

def sugar(x): 
    return sugar_calorie*x

def lentils(x): 
    return lentils_calorie*x

def carrot(x): 
    return carrot_calorie*x

def milk(x): 
    return milk_calorie*x

def potato(x): 
    return potato_calorie*x

def curd(x):
    return curd_calorie*x

def goat_blood(x):
    return goat_blood_calorie*x


print("\n############### Food Calorie and Protein Calculator!! ################### \n")
print("Choose a food: ")
print("1. For Orange")
print("2. For Chicken Breast")
print("3. For Chicken Liver")
print("4. For Sugar")
print("5. For Lentils")
print("6. For Carrot")
print("7. For Milk")
print("8. For Potato")
print("9. For Curd")
print("10. Goat Blood")
print("\n#########################################################################\n")


while True: 

    choice = input("[1/2/3/4/5/6/7/8/9/10]: ")

    try: 
        weight = float(input("Enter weight, in grams: "))

    except ValueError: 
        print("Input Error")

    if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']: 

        if choice == '1': 
            print("Total calories are: ", orange(weight), "and the protein content is, ", orange_protein_fun(weight), "g" )

        elif choice == '2': 
            print("Total calories are: ", chicken_breast(weight), "kcal")

        elif choice == '3': 
            print("Total calories are: ", chicken_liver(weight), "kcal")

        elif choice == '4': 
            print("Total calories are: ", sugar(weight), "kcal")

        elif choice == '5': 
            print("Total calories are: ", lentils(weight), "kcal")

        elif choice == '6': 
            print("Total calories are: ", carrot(weight), "kcal")

        elif choice == '7': 
            print("Total calories are: ", milk(weight))

        elif choice == '8': 
            print("Total calories are: ", potato(weight))

        elif choice == '9': 
            print("Total calories are: ", curd(weight))

        elif choice == '10': 
            print("Total Calories: ", goat_blood_calorie(weight))

        next = input("Calculate again? [y/n]: ")
        if next == "n": 
            break

    else: 
        print("Wrong Output")