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
    print("Please insert coins.")
    pennies = input("How many pennies?: ")
    nickles = input("How many nickles?: ")
    dimes = input("How many dimes?: ")
    quarters = input("How many quarters?: ")

    #Calcular total de dinero introducido
    money_in = PENNIE * float(pennies) + NICKLE * float(nickles) + DIME * float(dimes) + QUARTER * float(quarters)

    return money_in

#MAIN function
def main():
    #1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​”

    #Declaramos variables
    money = 0

    #Bucle para mostrar menú
    while(True):
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