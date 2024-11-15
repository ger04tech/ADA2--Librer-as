import quicksort_module
import shellsort_module
import radixsort_module
import heapsort_module

def inp():
    while True:
        try:
            tamaño = int(input("¿Cuántos elementos quieres ordenar? "))
            if tamaño > 0:
                break
            else:
                print("Por favor, ingresa un número entero positivo.")
        except ValueError:
            print("Por favor, introduce un número entero.")

    lista = []
    print("Introduce los elementos para ordenar (números o palabras):")
    for _ in range(tamaño):
        entrada = int(input("Elemento: "))
        lista.append(entrada)

    return lista

def main():
    hi = True
    a = inp()
    print(f"Lista original: {a}")

    while hi:
        sort = input("Seleccione el método de ordenamiento: A- Quicksort    B- Shellsort    C- Radix    D- Heap\n").upper()

        if sort == "A":
            b = quicksort_module.quicksort(a.copy())
            print(f"Lista ordenada con Quicksort: {b}")

        elif sort == "B":
            d = shellsort_module.shellsort(a.copy())
            print(f"Lista ordenada con Shellsort: {d}")

        elif sort == "C":
            e = radixsort_module.radix_sort(a.copy())
            print(f"Lista ordenada con Radix Sort: {e}")

        elif sort == "D":
            f = heapsort_module.heap_sort(a.copy())
            print(f"Lista ordenada con Heap Sort: {f}")

        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
