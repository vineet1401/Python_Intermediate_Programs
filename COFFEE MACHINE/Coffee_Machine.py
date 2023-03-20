import time


class StartMenu:

    def __init__(self):
        self.resources = {"Water": 200, "Milk": 100, "Coffee": 100, "Cost": 0}
        self.espresso = {"Water": 100, "Milk": 0, "Coffee": 15, "Cost": 20}
        self.latte = {"Water": 100, "Milk": 50, "Coffee": 25, "Cost": 30}
        self.cappuccino = {"Water": 50, "Milk": 100, "Coffee": 25, "Cost": 40}

    def Maintain_Machine(self, choice):
        if (choice == "Espresso"):
            self.resources["Water"] -= self.espresso["Water"]
            self.resources["Milk"] -= self.espresso["Milk"]
            self.resources["Coffee"] -= self.espresso["Coffee"]
            self.resources["Cost"] += self.espresso["Cost"]
        elif (choice == "Latte"):
            self.resources["Water"] -= self.latte["Water"]
            self.resources["Milk"] -= self.latte["Milk"]
            self.resources["Coffee"] -= self.latte["Coffee"]
            self.resources["Cost"] += self.latte["Cost"]
        elif (choice == "Cappuccino"):
            self.resources["Water"] -= self.cappuccino["Water"]
            self.resources["Milk"] -= self.cappuccino["Milk"]
            self.resources["Coffee"] -= self.cappuccino["Coffee"]
            self.resources["Cost"] += self.cappuccino["Cost"]
        else:
            pass

    def Get_Report(self):
        print("Resources-: ")
        print(f"Water: {self.resources['Water']}ml")
        print(f"Milk: {self.resources['Milk']}ml")
        print(f"Coffee: {self.resources['Coffee']}g")
        print(f"Money: {self.resources['Cost']}")


class CoffeeProcess():
    def __init__(self):
        StartMenu.__init__(self)

    def Display_Menu(self):
        self.choice = input(
            "Espresso - 20 Rs \nLatte - 30 Rs \nCappuccino - 40 Rs \nGet Report \nOff \n\t-->").capitalize()

    def Check_Ingredient(self, choice):
        if (choice == "Espresso"):
            if (self.resources["Water"] > self.espresso["Water"] and self.resources["Milk"] > self.espresso["Milk"] and self.resources["Coffee"] > self.espresso["Coffee"]):
                print("Ingredients Available")
                return True
            else:
                print("Insufficient Ingredients")
            return False
        elif (choice == "Latte"):
            if (self.resources["Water"] > self.latte["Water"] and self.resources["Milk"] > self.latte["Milk"] and self.resources["Coffee"] > self.latte["Coffee"]):
                print("Ingredients Available")
                return True
            else:
                print("Insufficient Ingredients")
        elif (choice == "Cappuccino"):
            if (self.resources["Water"] > self.cappuccino["Water"] and self.resources["Milk"] > self.cappuccino["Milk"] and self.resources["Coffee"] > self.cappuccino["Coffee"]):
                print("Ingredients Available")
                return True
            else:
                print("Insufficient Ingredients")
        else:
            pass

    def Collect_Money(self):
        self.deposit = int(input("Insert Money: "))

    def Make_Coffee(self, choice):
        if (choice == "Espresso"):
            if (self.deposit >= self.espresso["Cost"]):
                print("Transaction Successful")
                print("-----------------------------------")
                time.sleep(5)
                print("Please collect your coffee......")
                change = self.deposit - self.espresso["Cost"]
                if (change > 0):
                    print(f"Please collect your {change} Rs as change")

            else:
                print("Transaction failed...")
                print("Please collect your money")

        if (choice == "Latte"):
            if (self.deposit >= self.latte["Cost"]):
                print("Transaction Successful")
                print("-----------------------------------")
                time.sleep(5)
                print("Please collect your coffee......")
                change = self.deposit - self.latte["Cost"]
                if (change > 0):
                    print(f"Please collect your {change} Rs as change")

            else:
                print("Transaction failed...")
                print("Please collect your money")

        if (choice == "Cappuccino"):
            if (self.deposit >= self.cappuccino["Cost"]):
                print("Transaction Successful")
                print("-----------------------------------")
                time.sleep(5)
                print("Please collect your coffee......")
                change = self.deposit - self.cappuccino["Cost"]
                if (change > 0):
                    print(f"Please collect your {change} Rs as change")

            else:
                print("Transaction failed...")
                print("Please collect your money")

    def Close_machine(self):
        if (self.choice == "Off"):
            print("Thank you.... \nMachine Shutting Down")
            return False


is_on = True
startmenu = StartMenu()
makecoffe = CoffeeProcess()

while is_on:
    makecoffe.Display_Menu()
    options = makecoffe.choice
    if (options == "Espresso"):
        is_on = makecoffe.Check_Ingredient(options)
        if (is_on):
            makecoffe.Collect_Money()
            makecoffe.Make_Coffee(options)
            startmenu.Maintain_Machine(options)
    elif (options == "Latte"):
        is_on = makecoffe.Check_Ingredient(options)
        if (is_on):
            makecoffe.Collect_Money()
            makecoffe.Make_Coffee(options)
            startmenu.Maintain_Machine(options)
    elif (options == "Cappuccino"):
        is_on = makecoffe.Check_Ingredient(options)
        if (is_on):
            makecoffe.Collect_Money()
            makecoffe.Make_Coffee(options)
            startmenu.Maintain_Machine(options)
    elif (options == "Report"):
        startmenu.Get_Report()
    elif (options == "Off"):
        is_on = makecoffe.Close_machine()
    else:
        print("Invalid choice...")
    print("- * -" * 20)


