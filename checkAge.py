# simple program to use control flow


# - You can vote
# - You can driver
# - you can't legally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!
# as a user I should be able to keep being prompted for input until I say 'exit'
#
# ## Acceptance Criteria
#
# * is a program that run continuously
# * handles strings and integers
# * has exist condition
# * all business logic works

# age = input("How old are you? ")
# driver_licence = input("Do you have driving license? Y/N ")
#
#
# def check_age():


check_age = True
while check_age:
    age = input("How old are you? ")
    if age.isdigit():
        age = int(age)
        age_check = False
    else:
        print("Please enter your age in digits")


check_licence = True
while check_licence:
    driver_licence = input("Do you have a driver's licence? Y/N ")
    if driver_licence in ("Y", "N"):
        licence_check = False
    else:
        print("Please answer 'Y' or 'N'")