# TASK 2:
# - Create menu
# - Display menu to a customer
# - add orders to a list
# - print orders to customer

menu_items = ["1: pizza margarita ", "2: mushroom risotto", "3: pumpkin soup", "4: tomato panini", "5: orange juice", "6: chocolate cake"]
order_list = 0

def menu():
    for item in menu_items:
        print(f"Menu item {item}")

print("--Restaurant Menu--")
menu()




