import os

pennies = int(input("how many pennies do you have there?: "))

dollars = pennies  // 100
pennies = pennies % 100
quarters = pennies // 25
pennies = pennies % 25
dimes = pennies // 10
pennies = pennies % 10
nickels = pennies // 5
pennies = pennies % 5

def CLEAR_CONSOLE():
    # Windows
    if os.name == "nt":
        return os.system('cls')

CLEAR_CONSOLE()

print("here is all the money you have")

print(("dollars = ") + str(dollars))
print(("quarters = ") + str(quarters))
print(("dimes = ") + str(dimes))
print(("nickels = ") + str(nickels))
print(("pennies = ") + str(pennies))