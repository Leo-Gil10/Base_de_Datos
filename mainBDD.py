import BDDPreparatoria as prep
import BDDUniversidad as uni 
import BDDSecundaria as secu
import BDDPrimaria as prim
#Importar las librerías necesarias
while True:
    print("Seleccione una opción:")
    print("1. Preparatoria")
    print("2. Universidad")
    print("3. Salir")
    
    opcion = input("Ingrese el número de la opción deseada: ")
    1
    if opcion == '1':
        prep.menu_preparatoria()

    elif opcion == '2':
        uni.menu_universidad()
    elif opcion == '3':
        secu.menu_secundaria()
    elif opcion == '4':
        prim.menu_primaria()
    elif opcion == '5':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")