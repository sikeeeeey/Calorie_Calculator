# this is for the appending process at the end
calorie_count = 0
protein_count = 0

#Calorie and Protein content in foods

# orange calorie and protein content. 
orange_calorie = 0.47
orange_protein = 0.009

# chicken breast calorie and protein content
chicken_breast_calorie = 1.20
chicken_breast_protein = 0.2275

# chicken liver calorie and protein content
chicken_liver_calorie = 1.19
chicken_liver_protein = 0.17

# sugar calorie and protein content
sugar_calorie= 3.87 
sugar_protein = 0.00

# lentils calorie and protein content
lentils_calorie = 3.54
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
goat_blood_calorie = 0.85
goat_blood_protein = 0.208

# onion calorie and protein content 
onion_calorie = 0.40
onion_protein = 0.011

# oil calorie and protein content 
oil_calorie = 8.84
oil_protein = 0.00

# white rice calorie and protein content
white_rice_calorie = 3.65
white_rice_protein = 0.07

# white rice(cooked) calories and protein content 
cooked_white_rice_calorie = 1.30
cooked_white_rice_protein = 0.027
# Calculation functions:

# Orange  
def orange(x): 
    return orange_calorie*x

def orange_protein_fun(x):
    return orange_protein*x 

# Chicken Breast
def chicken_breast(x): 
    return chicken_breast_calorie*x

def chicken_breast_protein_fun(x):
    return chicken_breast_protein*x 

# Chicken Liver
def chicken_liver(x): 
    return chicken_liver_calorie*x

def chicken_liver_protein_fun(x):
    return chicken_liver_protein*x 

# Sugar
def sugar(x): 
    return sugar_calorie*x

def sugar_protein_fun(x):
    return sugar_protein*x 

# Lentils
def lentils(x): 
    return lentils_calorie*x

def lentils_protein_fun(x):
    return lentils_protein*x 

#Carrot
def carrot(x): 
    return carrot_calorie*x

def carrot_protein_fun(x):
    return carrot_protein*x 

# Milk
def milk(x): 
    return milk_calorie*x

def milk_protein_fun(x):
    return milk_protein*x 

# Potato
def potato(x): 
    return potato_calorie*x

def potato_protein_fun(x):
    return potato_protein*x 

# Curd
def curd(x):
    return curd_calorie*x

def curd_protein_fun(x):
    return curd_protein*x 

# Goat Blood
def goat_blood(x):
    return goat_blood_calorie*x

def goat_blood_protein_fun(x):
    return goat_blood_protein*x 

# Onion
def onion(x):
    return onion_calorie*x

def onion_protein_fun(x):
    return onion_protein*x 

# Oil
def oil(x):
    return oil_calorie*x

def oil_protein_fun(x):
    return oil_protein*x 


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
print("9. Curd")
print("10. Goat Blood")
print("11. Onion ")
print("12. Oil")

print("\n#########################################################################\n")


while True: 

    choice = input("[1/2/3/4/5/6/7/8/9/10/11/12]: ")

    try: 
        weight = float(input("\nEnter weight, in grams: "))

    except ValueError: 
        print("Input Error")

    if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']: 

        if choice == '1': 
            final_calorie = orange(weight)
            final_protein = orange_protein_fun(weight) 
            print("Calorie: ", final_calorie, "kcal", "\nProtein:", final_protein, "g" )

        elif choice == '2': 
            final_calorie = chicken_breast(weight)
            final_protein = chicken_breast_protein_fun(weight)
            print("Calorie: ", final_calorie, "kcal", "\nProtein:", final_protein, "g" )

        elif choice == '3': 
            final_calorie = chicken_liver(weight)
            final_protein = chicken_liver_protein_fun(weight)
            print("Calorie: ", final_calorie, "kcal", "\nProtein:", final_protein, "g" )

        elif choice == '4': 
            final_calorie = sugar(weight)
            final_protein = sugar_protein_fun(weight)
            print("Calorie: ", final_calorie, "kcal", "\nProtein:", final_protein, "g" )

        elif choice == '5':
            final_calorie = lentils(weight)
            final_protein = lentils_protein_fun(weight) 
            print("Calorie: ", final_calorie, "kcal", "\nProtein:", final_protein, "g" )

        elif choice == '6': 
            final_calorie = carrot(weight)
            final_protein = carrot_protein_fun(weight) 
            print("Calorie: ", final_calorie, "kcal", "\nProtein:", final_protein, "g" )

        elif choice == '7': 
            final_calorie = milk(weight)
            final_protein = milk_protein_fun(weight) 
            print("Calorie: ", final_calorie, "kcal", "\nProtein:", final_protein, "g" )

        elif choice == '8': 
            final_calorie = potato(weight)
            final_protein = potato_protein_fun(weight) 
            print("Calorie: ", final_calorie, "kcal", "\nProtein:", final_protein, "g" )

        elif choice == '9': 
            final_calorie = curd(weight)
            final_protein = curd_protein_fun(weight) 
            print("Calorie: ", final_calorie, "kcal", "\nProtein:", final_protein, "g" )

        elif choice == '10': 
            final_calorie = goat_blood(weight)
            final_protein = goat_blood_protein_fun(weight) 
            print("Calorie: ", final_calorie, "kcal", "\nProtein:", final_protein, "g" )

        elif choice == '11': 
            final_calorie = onion(weight)
            final_protein = onion_protein_fun(weight) 
            print("Calorie: ", final_calorie, "kcal", "\nProtein:", final_protein, "g" )

        elif choice == '12': 
            final_calorie = oil(weight)
            final_protein = oil_protein_fun(weight) 
            print("Calorie: ", final_calorie, "kcal", "\nProtein:", final_protein, "g" )

        append = input("\nDo you want to add this to your caloire count? [y/n]: ")
        if append == "y":
            calorie_count += final_calorie
            protein_count += final_protein
            print("\n Total Calorie Count: ", calorie_count, "kcal" "\n Total Protein Count: ", protein_count, "g\n")
        else: 
            next= input("\n Do you want to calculate again? [y/n]: ")
            if next == "n": 
                break;

    else: 
        print("Wrong Output")