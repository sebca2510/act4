estaciones = {'1': "calle 72", '2': "calle76", '3': "heroes", '4': "Escuela militar", '5': "Av.Boyaca"}

ruta1 = [estaciones['1'], estaciones['2']]
ruta2 = [estaciones['1'], estaciones['3']]
ruta3 = [estaciones['2'], estaciones['3']]
ruta4 = [estaciones['3'], estaciones['4']]
ruta5 = [estaciones['4'], estaciones['2']]
ruta6 = [estaciones['3'], estaciones['5']]
ruta7 = [estaciones['4'], estaciones['5']]

print("Los tiempos de cada ruta son: ")
print("\n", "1 minuto entre: ", ruta1 )
print("\n", "5 minutos entre: ", ruta2)
print("\n", "2 minutos entre: ", ruta3)
print("\n", "3 minutos entre: ", ruta4)
print("\n", "6 minutos entre: ", ruta5)
print("\n", "7 minutos entre: ", ruta6)
print("\n", "4 minutos entre: ", ruta7)

print("\n", "portanto la ruta mas rapida para llegar de %s a %s" %(estaciones["1"], estaciones["5"]), "es: ")
print("\n", ruta1, "posterior", ruta3, "posterior", ruta4, "posterior", ruta7)
print("\n","Tardando un total de 10 minutos ")
