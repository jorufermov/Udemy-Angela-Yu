#Day 15. Coffee Machine Program

from data import MENU, resources

#1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​”

#Declaramos variables
money = 0

#Bucle para mostrar menú
while(True):
    option = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

    #Acciones segun opcion escogida
    match option:
        case "espresso" | "latte" | "cappuccino":
            #Preparar cafés
            pass

        case "report":
            #Sacar reporte
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")

        case "off":
            #Apagar maquina de café
            exit()