from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = Menu()
coffee_machine = CoffeeMaker()
payment = MoneyMachine()
# order_amount = MenuItem()
working = True

while working:
    drink_choice = input(f'What would you like to order: {order.get_items()}')
    if drink_choice == "off":
        working = False
    elif drink_choice == "report":
        coffee_machine.report()
        payment.report()

    else:
        drink = order.find_drink(drink_choice)
        if coffee_machine.is_resource_sufficient(drink):
            print("We can make that!")
            cost = drink.cost
            payment.make_payment(cost)
            coffee_machine.make_coffee(drink)


