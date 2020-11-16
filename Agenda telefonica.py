#Buscar un numero de telefono por nombre exacto
#Listar todos lo numeros de telefono guardados
#Agregar un nuevo contacto(nombre y numero de telefono)

nombres_telefonos = {"Sebastian": 72950198,"Alvaro":88370170,"Abigail": 63300881,}

consulta = True
while consulta: #Menu de la agenda
    print()
    print("_____________________________________")
    print("**Agenda**")
    print("_____________________________________")
    print("1. Buscar Contacto")
    print("2. Agregar contacto")
    print("3. Ver contactos")
    print("4. Salir")
    print("_____________________________________")

    opcion = ""
    while opcion not in ("1","2","3","4"):
        opcion = input ("--->>")
    if opcion == "1": #Opcion dada en el menu
        nombre = input("Nombre:")
        if nombre not in nombres_telefonos:
            print("Nombre no existente.")
        else:
             telf = nombres_telefonos[nombre]
             print(nombre, ":", telf)

    elif  opcion =="2":#Opcion dada en el menu
        nombre = input ("Nombre:")
        if nombre in nombres_telefonos:
            print ("Contacto exitente.")
        else: telf = int(input("Numero de telefono:"))
        nombres_telefonos [nombre] = telf
        print("Contacto Añadido.")

    elif opcion == "3":#Opcion dada en el menu
            print("Ver contactos")
            print( nombres_telefonos)

    elif opcion == "4":#Opcion dada en el menu
        print("Chao, ha salido de la agenda")
        consulta = False
