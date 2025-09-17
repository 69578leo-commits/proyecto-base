from clases.operaciones import Operaciones

def main():
    op = Operaciones()

    while True:
        print("\n===== CALCULADORA BÁSICA =====")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "5":
            print("Saliendo... ¡Adiós!")
            break

        op.leerNumeros()

        if opcion == "1":
            op.sumar()
        elif opcion == "2":
            op.restar()
        elif opcion == "3":
            op.multiplicar()
        elif opcion == "4":
            op.dividir()
        else:
            print("Opción inválida.")
            continue

        op.mostrarResultado()

if __name__ == "__main__":
    main()
