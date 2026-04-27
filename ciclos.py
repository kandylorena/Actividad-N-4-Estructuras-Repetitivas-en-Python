 #1. Uso básico de while

contador = 1  #punto de partida del contador
while contador <=5:  
    print(contador)
    contador = contador+1

#2. Uso básico de for

frutas = ["manzana", "plátano", "naranja"]
for i in frutas:
    print(frutas)

# 3. Condición en un ciclo

for numero in range(1, 11):
    if numero % 2 ==0:
        print("Par")
    else:
        print("Impar")

#4. Ciclo infinito controlado con break

while True:
    numero = int(input("ingresa un numero o 0 para salir"))
    if numero == 0:
        print("Saliste")
        break
    else:
        print(f"numero ingresado {numero}")

#5. Ciclo anidado

for tabla in range (1, 4): 
    print(tabla)
    for resultado in range(1, 11):
        resultado_final = tabla * resultado
        print(f"{tabla} * {resultado} = {resultado_final}")
   
#6. Uso de continue
lista_nombres = ["Pedro", "Juan", "Diego"]#defino lista de nombres
for i in lista_nombres: # ciclo para recorrer los nombres
    if i == "Juan": # el nombre sea igual al Juan
        continue #omite a juan y continua al siguiente 
    print(i)