# TASK 2:
# - Create menu
# - Display menu to a customer
# - add orders to a list
# - print orders to customer

menu_items = ["1: pizza margarita ", "2: mushroom risotto", "3: pumpkin soup", "4: tomato panini", "5: orange juice", "6: chocolate cake"]


def menu():
    for item in menu_items:
        print(f"Menu item {item}")
print("--Restaurant Menu--")
print(menu())



completed_order = []


print("When you ordered everything you wanted write 'done'")
order = True
while order:
    user_order = input("What else would you like to order:  ")
    if user_order == "done":
        order = False
        break
    completed_order.append(user_order)

print(completed_order)

