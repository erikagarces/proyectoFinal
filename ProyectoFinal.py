# Inicializamos un diccionario para almacenar los contactos
contactos = {}

def agregar_contacto(nombre, numeros):
    """Agrega un nuevo contacto a la lista."""
    contactos[nombre] = numeros

def ver_contactos():
    """Muestra la lista de contactos."""
    print("\nLista de contactos:")
    for nombre, numeros in contactos.items():
        print(f"{nombre}: {', '.join(numeros)}")

def buscar_contacto(nombre):
    """Busca un contacto por nombre y muestra sus números."""
    if nombre in contactos:
        print(f"\nContacto encontrado - {nombre}: {', '.join(contactos[nombre])}")
    else:
        print(f"\nNo se encontró ningún contacto con el nombre '{nombre}'.")

def eliminar_contacto(nombre):
    """Elimina un contacto de la lista."""
    if nombre in contactos:
        del contactos[nombre]
        print(f"\nEl contacto '{nombre}' ha sido eliminado.")
    else:
        print(f"\nNo se encontró ningún contacto con el nombre '{nombre}'.")

while True:
    print("\nOpciones:")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")
