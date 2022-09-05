cislo1 = input("Zadejte cislo: ")
cislo2 = input("Zadejte cislo2: ")
cislo3 = input("Zadejte cislo3: ")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: 
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(cislo1, cislo2, cislo3))