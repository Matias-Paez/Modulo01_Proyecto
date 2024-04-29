#Funciones auxiliares....
val_telefono = lambda telefono: len(telefono) <= 10

def val_correo(correo):
    if '@' in correo and '.' in correo:
        return True
    else:
        return False
    
def verificar_contactos(contactos):
    if not contactos:
        print("No hay contactos disponibles.")
        return True
    return False

#Funciones propias del programa....

#MODIFICAR CONTACTO -------------------------------------------------------------------

def modificar_contacto(contactos):

    verificar_contactos(contactos)
    
    nombre = input("('x' para volver al menú principal)\nIngrese el nombre del contacto que desea modificar: ")
    
    if nombre.lower() == 'x':
        print ("Volviendo al menú principal.")
        return
    
    encontrado = False
    for contacto in contactos:
        if contacto['nombre'] == nombre:
            n_apellido = input("Ingrese el nuevo apellido: ")
            if n_apellido:
                contacto['apellido'] = n_apellido
            
            n_telefono = ("Ingrese el nuevo telefono: ")
            if n_telefono:
                contacto['telefono'] = n_telefono

            n_correo = ("Ingrese el nuevo correo: ")
            if n_correo:
                contacto['telefono'] = n_correo
            
            print("El contacto ha sido modificado con éxito!")
            encontrado = True
    
    if not encontrado:
        print("El contacto no existe en su lista.\nIntente de nuevo.")
        modificar_contacto(contactos)

#AGREGAR CONTACTO -------------------------------------------------------------------
def agregar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto: ")
    apellido = input("Ingrese el apellido del contacto: ")
    telefono = input("Ingrese el teléfono del contacto (Máx. 10 caractereres): ")
    while not val_telefono(telefono):
        telefono = input("Por favor ingrese un teléfono correcto.\n(Máx. 10 caractereres): ")
    correo = input("Ingrese un correo de contacto,\n(Formato correo@gmail.com): ")
    while not val_correo(correo):
        correo = input("Por favor ingrese un email correcto.\n(Formato correo@gmail.com): ")
    
    nuevo_contacto = {
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'correo': correo

    }

    contactos.append(nuevo_contacto)
    print("Contacto agregado con éxito.")


#ELIMINAR CONTACTO -------------------------------------------------------------------

def eliminar_contacto(contactos):
    
    verificar_contactos(contactos)

    nombre = input("'x', para volver al menú principal)\nIngrese el nombre del contacto que desea eliminar: ")

    if nombre.lower() == 'x':
        print ("Volviendo al menú principal.")
        return
    
    encontrado = False

    for contacto in contactos:
        if contacto['nombre'] == nombre:
            contactos.remove(contacto)
            print("Contacto eliminado correctamente.")
            encontrado=True
            break

    if not encontrado:
        print("El contacto no existe en su lista.\nIntente de nuevo")
        eliminar_contacto(contactos)
#BUSCAR CONTACTO -------------------------------------------------------------------

def buscar_contacto(contactos):
    
    verificar_contactos(contactos)
    
    nombre =input("('x', para volver al menú principal)\nIngrese el nombre del contacto que desea buscar.")
    
    if nombre.lower() == 'x':
        print ("Volviendo al menú principal.")
        return
    
    encontrado = False

    for contacto in contactos:
        if contacto['nombre'] == nombre:
            print ("\n---Información del Contacto---")
            print (f"---Nombre: {contacto['nombre']}---")
            print (f"---Apellido: {contacto['apellido']}---")
            print (f"---Teléfono: {contacto['telefono']}---")
            print (f"---Correo: {contacto['correo']}---")
            print ("------------------------------\n")

            encontrado = True
            break

    if not encontrado:
        print ("E contacto no existe en su lista.\nIntente de nuevo")
        buscar_contacto(contactos)


#LISTAR CONTACTOS -------------------------------------------------------------------

def listar_contactos(contactos):
    if verificar_contactos(contactos):
        return
    
    print("Lista de contactos:")
    for i, contacto in enumerate(contactos, start=1):
        print(f"{i + 1}. Nombre: {contacto['nombre']}, Apellido: {contacto['apellido']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}\n")



