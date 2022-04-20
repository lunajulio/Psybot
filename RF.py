#Requerimiento funcional: Registro de pensamientos.
#Se usara un archivo en el cual cada entrada nueva sera registro nuevo

file = open("Pensamientos.txt", "w") #Escribir la ruta
file.write("")
print("Hola! Porfavor decide que deseas hacer: /n 1. Escribir nueva entrada /n 2. Ver entradas anteriores")
des = input()
if des == 1 :
    print("Porfavor escribe que piensas")
    temp = input()
    file.write(temp + "/n")
    file.close()
elif des == 2:
    file.open("Pensamientos.txt", "r")
    temp2 = file.read()
    print(temp2)
    file.close()
