from sympy import symbols, sqrt, nsimplify
from pystyle import Write, Colors , Colorate

a = symbols('a')
b = symbols('b')
delta = symbols('delta')

print(" -----------------------------------------------------------")
print("|             *********************************             |")
print("|                 Equation du second degrès                 |") 
print("|             *********************************             |")
print(" -----------------------------------------------------------\n\n")

print("Resout les equations de la forme:\n (1) ax² + bx + c = 0 \n (2) ax + b = 0 \n\n")


def affine(): 
        a_val = input("  a: ")
        b = input("  b: ")
        print("")
        x1 = -int(a_val) / int(b)
        print(f"- L'unique solution de cette equation est {x1}\n")
        equations()
        


def second_degres():
    while True:
        # Récupération des réels a, b et c de l'expression ax² + bx + c
        a_val = input("  a: ") 
        b_val = input("  b: ")
        c = input("  c: ")
        print("")

        if int(a_val) == 0:
            x1 = -int(b_val) / int(c)
            print(f"- L'unique solution de cette equation est x = {x1}\n")
            equations()


        # Calcul de Delta
        delta_val = (int(b_val) ** 2) - (4 * int(a_val) * int(c))

        # Si delta est égal à 0 alors l'équation admet une unique solution dans R
        if int(delta_val) == 0:
            x1 = -int(b_val) / (2 * int(a_val))
            print(f"- L'unique solution est x = {x1}\n")
            equations()

        # Si delta est inférieur alors elle n'admet aucune solution dans R
        elif int(delta_val) < 0:
            # color = (Colors.green + str(delta_val))
            print(f"- Delta vaut {delta_val} il n'admet donc aucune racine dans R \n")

            # Calcul des solutions complexes
            an = Write.Input("[?] Voulez-vous les solutions dans C ? y/n: ", Colors.red_to_purple, interval=0.0015)
            if an == "y":
                solution1 = (-b - sqrt(-delta)) / (2 * a)
                solution2 = (-b + sqrt(-delta)) / (2 * a)
                solution1 = nsimplify(solution1.evalf(subs={a: int(a_val), b: int(b_val), delta: -int(delta_val)}))
                solution2 = nsimplify(solution2.evalf(subs={a: int(a_val), b: int(b_val), delta: -int(delta_val)}))
                print(f"- Les solutions complexes sont: c1 = {solution1} et c2 = {solution2}\n")
                equations()
            else:
                equations()

        # Si delta est supérieur à 0 alors elle admet deux solutions distinctes dans R
        elif int(delta_val) > 0:
            x1 = (-int(b_val) + sqrt(int(delta_val))) / (2 * int(a_val))
            x2 = (-int(b_val) - sqrt(int(delta_val))) / (2 * int(a_val))
            print(f"- Les solutions sont: x1 = {x1} et x2 = {x2}\n")
            equations()

def equations():
        type = Write.Input("[?] Equation (1 ou 2):  ", Colors.blue_to_purple, interval=0.0015)
        # type = input ("[?] Equation (1 ou 2):  ")  
        print("")
        if type == "1":
                second_degres()
        elif type == "2":
                affine()
        else:
            print(Colors.red + "!!!! Choisit entre 1 et 2 !!!! \n")
            print(Colors.white + "")
            equations
equations()

