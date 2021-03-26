# TASK 2:
# - Create menu
# - Display menu to a customer
# - add orders to a list
# - print orders to customer

menu_items = ["1: pizza margarita ", "2: mushroom risotto", "3: pumpkin soup", "4: tomato panini", "5: orange juice", "6: chocolate cake"]
user_order = input("What would you like to order?")
completed_order = []

def menu():
    for item in menu_items:
        print(f"Menu item {item}")

print("--Restaurant Menu--")
print(menu())
print(user_order)
def order():
    for i in range(0,user_order):
        completed_order.append(int(input()))



