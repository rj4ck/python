num_1 = int(input("Escoge un entero: "))
num_2 = int(input("Escoge otro entero: "))

if (num_1 > num_2):
    print("El primero numero es mayor que el segundo")
elif num_1 < num_2:
    print("El segundo numero es mayor que el primero")
else:
    print("Los dos numeros son iguales")


#-----------------------

name_person_1 = input('Nombre de la primera persona: ')
age_person_1 = int(input('Edad de la primera persona: '))

name_person_2 = input('Nombre de la segunda persona: ')
age_person_2 = int(input('Edad de la segunda persona: '))

if (age_person_1 > age_person_2):
    print(f'{name_person_1} es mayor que {name_person_2}')
elif age_person_1 < age_person_2:
    print(f'{name_person_2} es mayor que {name_person_2}')
else:
    print(f'{name_person_1} y {name_person_2} son de la misma edad')