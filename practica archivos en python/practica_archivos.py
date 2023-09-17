alumnos = [
    "Juan,98,87,89,90",
    "Jose,90,43,20,40",
    "Pedro,70,80,89,90"
]

#Función para calcular el promedio de las notas de un estudiante
def calcular_promedio_de_las_notas(notas):
#nos devuelve el valor del resultado del promedio 
    return sum(notas) / len(notas)
calcular_promedio_de_las_notas()

#Procesar la lista de alumnos y calcular los promedios
promedios = {}
for alumno in alumnos:
    datos = alumno.split(',')
    nombre = datos[0]
#La funcion map sirve como una especie de iterador que se pueda aplicar a cada elemento de una lista, tupla, etc
    notas = list(map(int, datos[1:]))
    promedio = calcular_promedio_de_las_notas(notas)
    promedios[nombre] = promedio

#Guardar los resultados en un archivo de texto
#La palabra clave with nos sirve para simplicar la gestion de recursos en los flujos de archivos, aparte puede servir como manejo de excepciones.
#La palabra clave as nos sirve para hacer o crear un alias para hacer referencia a algo en nuestro programa. 
with open("promedios.txt", "w") as archivo:
#El metodo de .items lo usamos para obtener las key-value de un diccionario
    for nombre, promedio in promedios.items():
#Con .2f le decimos que las cantidades enteras les agregue dos decimales para volverlo un float
        archivo.write(f"{nombre}={promedio:.2f}\n")

print("Los promedios se han guardado en el archivo 'promedios.txt'")