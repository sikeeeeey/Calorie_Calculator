# orange calorie and protein content. 
orange_calorie = 0.47
orange_protein = 0.009

# chicken breast calorie and protein content
chicken_breast_calorie = 1.65
chicken_breast_protein = 0.31

# chicken liver calorie and protein content
chicken_liver_calorie = 1.67
chicken_liver_protein = 0.24

# sugar calorie and protein content
sugar_calorie= 3.87 
sugar_protein = 0.00

# lentils calorie and protein content
lentils_calorie = 3.44
lentils_protein = 0.26

# carrot  calorie and protein content 
carrot_calorie = 0.41
carrot_protein = 0.09

# milk calorie and protein content 
milk_calorie = 0.67
milk_protein = 0.033

# potato calorie and protein content
potato_calorie = 0.77
potato_protein = 0.02

# curd calorie and protein content 
curd_calorie = 0.98
curd_protein = 0.10

# goat blood calorie and protein content 
goat_blood_calorie = 0.80
goat_blood_protein = 0.21

def orange(x): 
    return orange_calorie*x

def orange_protein_fun(x):
    return orange_protein*x 

def chicken_breast(x): 
    return chicken_breast_calorie*x

def chicken_breast_protein_fun(x):
    return chicken_breast_protein*x 

def chicken_liver(x): 
    return chicken_liver_calorie*x

def chicken_liver_protein_fun(x):
    return chicken_liver_protein*x 

def sugar(x): 
    return sugar_calorie*x

def sugar_protein_fun(x):
    return sugar_protein*x 

def lentils(x): 
    return lentils_calorie*x

def lentils_protein_fun(x):
    return orange_protein*x 

def carrot(x): 
    return carrot_calorie*x

def carrot_protein_fun(x):
    return carrot_protein*x 

def milk(x): 
    return milk_calorie*x

def milk_protein_fun(x):
    return milk_protein*x 

def potato(x): 
    return potato_calorie*x

def potato_protein_fun(x):
    return potato_protein*x 

def curd(x):
    return curd_calorie*x

def curd_protein_fun(x):
    return curd_protein*x 

def goat_blood(x):
    return goat_blood_calorie*x

def goat_blood_protein_fun(x):
    return goat_blood_protein*x 


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
        weight = float(input("\nEnter weight, in grams: "))

    except ValueError: 
        print("Input Error")

    if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']: 

        if choice == '1': 
            print("Calorie: ", orange(weight), "kcal", "\nProtein:", orange_protein_fun(weight), "g" )

        elif choice == '2': 
            print("Calories: ", chicken_breast(weight), "kcal", "\nProtein:", chicken_breast_protein_fun(weight), "g" )

        elif choice == '3': 
            print("Calories: ", chicken_liver(weight), "kcal" "\nProtein:", chicken_liver_protein_fun(weight), "g")

        elif choice == '4': 
            print("Calories: ", sugar(weight), "kcal",  "\nProtein:", sugar_protein_fun(weight), "g")

        elif choice == '5': 
            print("Calories: ", lentils(weight), "kcal",  "\nProtein:", lentils_protein_fun(weight), "g")

        elif choice == '6': 
            print("Calories: ", carrot(weight), "kcal", "\nProtein:", carrot_protein_fun(weight), "g")

        elif choice == '7': 
            print("Calories: ", milk(weight), "kcal", "\nProtein:", milk_protein_fun(weight), "g")

        elif choice == '8': 
            print("Calories: ", potato(weight), "kcal", "\nProtein:", potato_protein_fun(weight), "g")

        elif choice == '9': 
            print("Calories: ", curd(weight), "kcal", "\nProtein:", curd_protein_fun(weight), "g")

        elif choice == '10': 
            print("Calories: ", goat_blood(weight), "kcal", "\nProtein:", goat_blood_protein_fun(weight), "g")

        next = input("\nCalculate again? [y/n]: ")
        if next == "n": 
            break

    else: 
        print("Wrong Output")