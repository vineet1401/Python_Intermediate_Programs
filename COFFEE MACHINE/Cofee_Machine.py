import time

# Resources int the coffee machine at initial stage
Resources = {"Water": 300, "Milk": 200, "Coffee": 100, "Coins": 0}

# Defining coffee prices and resources left
Espresso = {"Water": 50, "Coffee": 18, "Coins": 1.50}
Latte = {"Water": 200, "Milk": 150, "Coffee": 24, "Coins": 2.50}
Cappuccino = {"Water": 250, "Milk": 100, "Coffee": 24, "Coins": 3.00}

# Function of Espresso coffee


def Make_Espresso(amt):
    '''Espresso coffee function user global Resorces and Espresso dictionary'''
    global Resources, Espresso
    # Coffee price is __ if the price is same then proceed
    if (amt == 1.50):
        # Confirming them to wait
        print("Processing !!!")
        # Check all the resources needed for the coffee and if resouces are available proceed
        if (Resources["Water"] > Espresso["Water"]):
            if (Resources["Coffee"] > Espresso["Coffee"]):
                # If all resources are available then reduce them from the initial resouces and add
                # Coin to the resources and give them the coffee
                print("Transaction Successful. Just wait for a While")
                Resources["Water"] -= Espresso["Water"]
                Resources["Coffee"] -= Espresso["Coffee"]
                time.sleep(3)
                print("........................")
                print("Please collect your coffee.")
                Resources["Coins"] += Espresso["Coins"]
        # if the resources are less display this message
        else:
            print("Insufficient Resource.")
            print("Transaction Failed")
            print(".................................")
            print("Please collect your coins.")
    # if the money is more or less display this message
    else:
        print("Insufficient or More money.")
        print("Transaction failed")
        print(".................................")
        print("Please collect your coins.")

# function for latte coffee


def Make_Latte(amt):
    '''Latte coffee function user global Resorces and Latte dictionary'''
    global Resources, Latte
    # Coffee price is __ if the price is same then proceed
    if (amt == 2.50):
        # Confirming them to wait
        print("Processing !!!")
        # Check all the resources needed for the coffee and if resouces are available proceed
        if (Resources["Water"] > Latte["Water"]):
            if (Resources["Coffee"] > Latte["Coffee"]):
                if (Resources["Milk"] > Latte["Milk"]):
                    # If all resources are available then reduce them from the initial resouces and add
                    # Coin to the resources and give them the coffee
                    print("Transaction Successful. Just wait for a While")
                    Resources["Water"] -= Latte["Water"]
                    Resources["Coffee"] -= Latte["Coffee"]
                    Resources["Milk"] -= Latte["Milk"]
                    time.sleep(3)
                    print("........................")
                    print("Please collect your coffee.")
                    Resources["Coins"] += Latte["Coins"]
    # if the resources are less display this message
        else:
            print("Insufficient Resource.")
            print("Transaction Failed")
            print(".................................")
            print("Please collect your coins.")
    # if the money is more or less display this message
    else:
        print("Insufficient or More money.")
        print("Transaction failed")
        print(".................................")
        print("Please collect your coins.")

# function for cappuccino coffee


def Make_Cappuccino(amt):
    '''Cappuccino coffee function user global Resorces and Cappuccino dictionary'''
    global Resources, Cappuccino
    # Coffee price is __ if the price is same then proceed
    if (amt == 3.00):
        # Confirming them to wait
        print("Processing !!!")
        # Check all the resources needed for the coffee and if resouces are available proceed
        if (Resources["Water"] > Cappuccino["Water"]):
            if (Resources["Coffee"] > Cappuccino["Coffee"]):
                if (Resources["Milk"] > Cappuccino["Milk"]):
                    # Coin to the resources and give them the coffee
                    # If all resources are available then reduce them from the initial resouces and add
                    print("Transaction Successful. Just wait for a While")
                    Resources["Water"] -= Cappuccino["Water"]
                    Resources["Coffee"] -= Cappuccino["Coffee"]
                    Resources["Milk"] -= Cappuccino["Milk"]
                    time.sleep(3)
                    print("........................")
                    print("Please collect your coffee.")
                    Resources["Coins"] += Cappuccino["Coins"]
    # if the resources are less display this message
        else:
            print("Insufficient Resource.")
            print("Transaction Failed")
            print(".................................")
            print("Please collect your coins.")
    # if the money is more or less display this message
    else:
        print("Insufficient or More coin.")
        print("Transaction failed")
        print(".................................")
        print("Please collect your coins.")

# Function for displaying the resources


def Report(dict):
    '''Dispay the resources in the inventory'''
    print("Resources left :")
    for key, value in dict.items():
        print(f"\t {key} : {value}")

# Function for collecting coin


def Collect_Coins():
    '''Collecting coin from user and returning the amount'''
    amount = 0
    penny = int(input("Enter number of penny coins: "))
    dime = int(input("Enter number of dime coins: "))
    nickel = int(input("Enter number of nickel coins: "))
    quarter = int(input("Enter number of quarter coins: "))

    amount += ((penny*0.01) + (dime*0.10) + (nickel*0.05) + (quarter*0.25))
    return amount


cond = True
while (cond):
    print("<------------------------------------------------------------------------->")
    print("Choose Your options : ")
    print("\t 1. Espresso - 30 Rs\n\t 2. Latte - 40 Rs\n\t 3. Cappuccino - 50 Rs\n\t 4. Report \n\t 0. Exit")
    choice = int(input("Your Choice? "))
    print("<------------------------------------------------------------------------->")
    time.sleep(2)
    time.sleep(2)
    if (choice == 1):
        amt = Collect_Coins()
        Make_Espresso(amt)
    elif (choice == 2):
        amt = Collect_Coins()
        Make_Latte(amt)
    elif (choice == 3):
        amt = Collect_Coins()
        Make_Cappuccino(amt)
    elif (choice == 4):
        Report(Resources)
    elif (choice == 0):
        cond = False
    else:
        print("Invalid Choice!")
    print("<------------------------------------------------------------------------->")
