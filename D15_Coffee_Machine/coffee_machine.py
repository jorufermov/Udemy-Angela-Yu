#Day 15. Coffee Machine Program

from data import MENU, resources

#Variables globales
PENNIE = 0.01
NICKLE = 0.05
DIME = 0.10
QUARTER = 0.25

#Declaración de funciones

#print report
def show_report(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

#Check resources
def check_resources(option):
    for ingredient in MENU[option]["ingredients"]:
        if resources[ingredient] < MENU[option]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

#insert coins
def insert_coins():
    try:
        print("Please insert coins.")
        pennies = int(input("How many pennies?: "))
        nickles = int(input("How many nickles?: "))
        dimes = int(input("How many dimes?: "))
        quarters = int(input("How many quarters?: "))
    except ValueError:
        pennies = 0
        nickles = 0
        dimes = 0
        quarters = 0
        print("Error inserting coins!!!")
        money_in = -1
        return money_in

    #Calcular total de dinero introducido
    money_in = PENNIE * pennies + NICKLE * nickles + DIME * dimes + QUARTER * quarters

    return money_in

#MAIN function
def main():
    #1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​”

    #Declaramos variables
    money = 0

    #Bucle para mostrar menú
    while(True):
        #Inicializamos a cero el dinero introducido
        money_in = 0
        option = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

        #Acciones segun opcion escogida
        match option:
            case "espresso" | "latte" | "cappuccino":
                #check enough resources
                if not check_resources(option):
                    continue
                #insert coins
                money_in = insert_coins()
                #Suficiente dinero??
                if money_in == -1:
                    continue
                if money_in < MENU[option]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                    continue

                #Si hay mas pasta de lo que vale se le devuelve el sobrante
                if money_in > MENU[option]["cost"]:
                    money_back = money_in - MENU[option]["cost"]
                    print(f"Here is ${money_back:.2f} in change.")

                #Actualizamos ingredientes
                for ingredient in MENU[option]["ingredients"]:
                    resources[ingredient] -= MENU[option]["ingredients"][ingredient]

                #Ingresamos pasta
                money += MENU[option]["cost"]
                #Servimos café
                print(f"Here is your {option}. Enjoy!")

            case "report":
                #Sacar reporte
                show_report(money)

            case "off":
                #Apagar maquina de café
                exit()
                
            case _:
                print("Opción no válida")


if __name__ == "__main__":
    main()
