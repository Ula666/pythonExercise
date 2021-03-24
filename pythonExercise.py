from datetime import date

# TASK 1: Program calculate year of birth!
age = int(input("Please enter your age: "))
name = input("Please enter your name: ")


def age_calculator(age, name):
    today = date.today().year
    birth_year = (today - age)

    print(f"OMG, {name}! You are {age} years old, so You were born in {birth_year} ")


age_calculator(age, name)




