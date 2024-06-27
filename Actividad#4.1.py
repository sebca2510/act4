directorio = {}

def getpro(ID):
    return directorio.get(ID, None)

def putpro(ID, proveedor):
    directorio[ID] = proveedor

def directorio_size():
    return len(directorio)

def is_directorio_empty():
    return len(directorio) == 0

def getpro_ID():
    return list(directorio.keys())

def getpro_list():
    return list(directorio.values())

def agrepro():
    ID = input("Ingrese la ID del provedor: ")
    nombre = input("Ingrese el nombre del provedor: ")
    direccion = input("Ingrese direccion del provedor: ")
    correro = input("ingrese la direccion de correo del provedor: ")

    provedor = {"ID": ID, "nombre": nombre, "direccion": direccion, "correo": correro}
    putpro(ID, provedor)
    print("provedor agregado exitosamenta")

while True:
    agrepro()
    mas = input("¿Quiere agregar otro proveedor? (S/N):")
    if mas.lower() != "S":
        break



print("Tamaño del directorio:", directorio_size())
print("¿El directorio está vacío?", is_directorio_empty())
print("NITs de los proveedores:", getpro_ID())
print("Proveedores:", getpro_list())