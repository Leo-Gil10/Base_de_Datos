# Mostrar alumnos
def mostrarAlumnos():
    print("Leo\nHeriberto\nLiam\nIan\nGauss\n") 
# Mostrar profesores
def mostrarProfesores():
    print("Sofia\nMateo\nValentina\nDiego\nCamila\n")
# Mostrar materias
def mostrarMaterias():
    print("Matematicas\nFisica\nQuimica\nBiologia\nHistoria\n")
# Materia de cada profesor
def MateriadeCadaProfesor():
    print ("Sofia: Matematicas\nMateo: Fisica\nValentina: Quimica\nDiego: Biologia\nCamila: Historia\n")
def CalificaiconesEnCadaMateriaDeCadaAlumno():
    print("Leo: Matematicas 90, Fisica 85, Quimica 88, Biologia 92, Historia 80\nHeriberto: Matematicas 78, Fisica 82, Quimica 80, Biologia 75, Historia 88\nLiam: Matematicas 85, Fisica 89, Quimica 90, Biologia 87, Historia 84\nIan: Matematicas 92, Fisica 95, Quimica 94, Biologia 90, Historia 91\nGauss: Matematicas 88, Fisica 84, Quimica 86, Biologia 89, Historia 87\n")
# Menú de Preparatoria
def menu_preparatoria():
    print("Menú de Preparatoria")
    print("Seleccione una opción:")
    print("1. Mostrar alumnos")
    print("2. Mostrar profesores")
    print("3. Mostrar materias")
    print("4. Mostrar materia de cada profesor")
    print("5. Mostrar calificaciones en cada materia de cada alumno")
    opcion = int(input("Ingrese el número de la opción deseada: "))
    match opcion:
        case 1:
            mostrarAlumnos()
        case 2:
            mostrarProfesores()
        case 3:
            mostrarMaterias()
        case 4:
            MateriadeCadaProfesor()
        case 5:     
            CalificaiconesEnCadaMateriaDeCadaAlumno()
        case _: # Caso por defecto
            print("Opción inválida")
