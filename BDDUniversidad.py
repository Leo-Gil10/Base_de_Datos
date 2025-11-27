# Mostrar alumnos
def mostrarAlumnos():
    return "Alice\n" 
    return "Bob\n" 
    return "Charlie\n"
    return "Diana\n"
    return "Eve\n"
# Mostrar profesores
def mostrarProfesores():
    return "Dr. Smith\n"
    return "Prof. Johnson\n"
    return "Dr. Williams\n"
    return "Prof. Brown\n"
    return "Dr. Jones\n"
# Mostrar materias
def mostrarMaterias():
    return "Ciencias de la Computación\n"
    return "Matemáticas Avanzadas\n"
    return "Física Cuántica\n"
    return "Biología Molecular\n"
    return "Historia del Arte\n"
def MateriadeCadaProfesor():
    return "Dr. Smith: Ciencias de la Computación\n"
    return "Prof. Johnson: Matemáticas Avanzadas\n"
    return "Dr. Williams: Física Cuántica\n"
    return "Prof. Brown: Biología Molecular\n"
    return "Dr. Jones: Historia del Arte\n"
#  Calificaciones en cada materia de cada alumno
def CalificaiconesEnCadaMateriaDeCadaAlumno():
    return "Alice: Ciencias de la Computación 95, Matemáticas Avanzadas 88, Física Cuántica 92, Biología Molecular 85, Historia del Arte 90\n"
    return "Bob: Ciencias de la Computación 78, Matemáticas Avanzadas 82, Física Cuántica 80, Biología Molecular 75, Historia del Arte 88\n"
    return "Charlie: Ciencias de la Computación 85, Matemáticas Avanzadas 89, Física Cuántica 90, Biología Molecular 87, Historia del Arte 84\n"
    return "Diana: Ciencias de la Computación 92, Matemáticas Avanzadas 95, Física Cuántica 94, Biología Molecular 90, Historia del Arte 91\n"
    return "Eve: Ciencias de la Computación 88, Matemáticas Avanzadas 84, Física Cuántica 86, Biología Molecular 89, Historia del Arte 87\n"
# Menú de Universidad
def menu_universidad():

    print("Menú de Universidad")
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
