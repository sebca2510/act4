usurarios = []

for i in range(20):
    nombre = input(f"Ingrese el nombre del usuario {i + 1}: ")
    usurarios.append(nombre)

usurarios = [nombre.lower() for nombre in usurarios]

usurarios.sort()

print("\nUsuarios en orden alfabético:")
for i, usuario in enumerate(usurarios, 1):
    print(f"{i}. {usuario}")

buscar = input("\nIngrese el nombre de usuario a buscar: ").lower()
if buscar in usurarios:
    posicion = usurarios.index(buscar) + 1
    print(f"{buscar} encontrado en la posición {posicion}.")
else:
    print(f"{buscar} no se encuentra en la lista.")