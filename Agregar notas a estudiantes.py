# nombre: Diego Fernando Madrid Monserrate

def agregar_estudiante(notas, nombre, nota):
    notas[nombre] = nota

def mostrar_notas(notas):
    print("--- Lista de notas ---")
    for nombre, nota in notas.items():
        print(f"{nombre}: {nota}")

def buscar_estudiante(notas, nombre):
    return notas.get(nombre, "No encontrado")

notas = {}
agregar_estudiante(notas, "Ana", 8.5)
agregar_estudiante(notas, "Luis", 7.0)
mostrar_notas(notas)
print(buscar_estudiante(notas, "Ana"))