from modulos.opc_menu import *

def salir():
    print("Saliendo del programa.")
    exit()

def opc_menu():
    print ("\n   ¡Bienvenido! \n")
    print ("1. Listar contactos.")
    print ("2. Agregar contacto.")
    print ("3. Modificar contacto.")
    print ("4. Eliminar contacto.")
    print ("5. Buscar contacto.")
    print ("6. Salir del programa.\n")

def opcion():
    while True:
        opcion = input("Seleccione una opción (1-6): ")
        if opcion.isdigit() and 1 <= int(opcion) <= 6:
            return int(opcion)
        else:
            print("Opción incorrecta. Intente nuevamente.")

def menu(contactos):
    opc_menu()
    opcion()

    if opcion() == 1:
            listar_contactos(contactos)
    elif opcion() == 2:
            agregar_contacto(contactos)
    elif opcion() == 3:
            modificar_contacto(contactos)
    elif opcion() == 4:
            eliminar_contacto(contactos)
    elif opcion() == 5:
            buscar_contacto(contactos)
    elif opcion() == 6:
            salir()