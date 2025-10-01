def crear_notas():
    """Crear lista de notas ingresadas por el usuario"""
    notas = []
    cantidad = int(input("¿Cuántas notas quiere ingresar? "))
    for i in range(cantidad):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i+1}: "))
                if 0 <= nota <= 100:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Ingrese un número válido.")
    return notas

def leer_notas(notas):
    """Mostrar notas actuales"""
    if notas:
        print("Notas actuales:", notas)
    else:
        print("Sin notas aún")

def actualizar_nota(notas):
    """Actualizar una nota específica"""
    leer_notas(notas)
    if notas:
        try:
            index = int(input("Ingrese la posición de la nota a actualizar (1,2,3...): ")) - 1
            if 0 <= index < len(notas):
                nueva_nota = float(input("Ingrese la nueva nota: "))
                if 0 <= nueva_nota <= 100:
                    notas[index] = nueva_nota
                    print("Nota actualizada")
                else:
                    print("La nota debe estar entre 0 y 100")
            else:
                print("Posición inválida")
        except ValueError:
            print("Ingrese un valor válido")

def eliminar_nota(notas):
    """Eliminar una nota"""
    leer_notas(notas)
    if notas:
        try:
            index = int(input("Ingrese la posición de la nota a eliminar (1,2,3...): ")) - 1
            if 0 <= index < len(notas):
                eliminado = notas.pop(index)
                print(f"Nota {eliminado} eliminada.")
            else:
                print("Posición inválida.")
        except ValueError:
            print("Ingrese un valor válido.")


def quitar_nota_mas_baja(notas):
    """Elimina la nota más baja para calcular promedio ajustado"""
    if len(notas) > 1:
        return sorted(notas)[1:] 
    return notas

def calcular_promedio(notas):
    """Calcula el promedio de las notas restantes"""
    if notas:
        promedio = sum(notas) / len(notas)
        return round(promedio, 2)
    return 0


def main():
    print("=== Sistema de Promedios de Estudiantes ===")
    codigo = input("Ingrese el código: ")
    notas = crear_notas()
    
    while True:
        print("\nOpciones:")
        print("1 - Ver notas")
        print("2 - Actualizar nota")
        print("3 - Eliminar nota")
        print("4 - Calcular promedio ajustado sin la nota más baja")
        print("5 - Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            leer_notas(notas)
        elif opcion == "2":
            actualizar_nota(notas)
        elif opcion == "3":
            eliminar_nota(notas)
        elif opcion == "4":
           
            notas_ajustadas = quitar_nota_mas_baja(notas)
            
            
            if len(notas_ajustadas) < 2:
                print("No hay suficientes notas para calcular promedio ajustado.")
            else:
                promedio_final = calcular_promedio(notas_ajustadas)
                print(f"\nNotas originales: {notas}")
                print(f"Notas sin la calificación más baja de todas: {notas_ajustadas}")
                print(f"Promedio ajustado {codigo}: {promedio_final}")
        elif opcion == "5":
            print("Saliendo del programa")
            break
        else:
            print("Intente otra vez")

main()