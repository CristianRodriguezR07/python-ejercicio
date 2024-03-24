class Persona:
    nombre = ""
    edad = 0
    total_personas = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.total_personas += 1

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    carrera = ""
    total_estudiantes = 0

    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        Estudiante.total_estudiantes += 1

    def imprimir_informacion(self):
        if isinstance(self, Persona):
            print(f"Nombre: {self.nombre}")
            print(f"Edad: {self.edad}")
        elif isinstance(self, Estudiante):
            print(f"Carrera: {self.carrera}")

class Profesor(Persona):
    especialidad = ""
    total_profesores = 0

    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
        Profesor.total_profesores += 1

    def imprimir_informacion(self):
        if isinstance(self, Persona):
            print(f"Nombre: {self.nombre}")
            print(f"Edad: {self.edad}")
        elif isinstance(self, Profesor):
            print(f"Especialidad: {self.especialidad}")

def registrar_persona():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    tipo_persona = input("Ingrese el tipo de persona (Estudiante/Profesor): ")
    carrera = None
    especialidad = None

    if tipo_persona.lower() == "estudiante":
        carrera = input("Ingrese la carrera: ")
    elif tipo_persona.lower() == "profesor":
        especialidad = input("Ingrese la especialidad: ")
    else:
        print("Tipo de persona no válida.")
        return

    if tipo_persona.lower() == "estudiante":
        persona = Estudiante(nombre, edad, carrera)
        print(f"Estudiante registrado: {persona.nombre}")
        print(f"Total estudiantes: {Estudiante.total_estudiantes}")
    elif tipo_persona.lower() == "profesor":
        persona = Profesor(nombre, edad, especialidad)
        print(f"Profesor registrado: {persona.nombre}")
        print(f"Total profesores: {Profesor.total_profesores}")

def mostrar_menu():
    print("-" * 20)
    print("Sistema de Gestión de Personas")
    print("-" * 20)
    print("1. Registrar persona")
    print("2. Salir")
    print("-" * 20)

def generar_informe():
    print("-" * 20)
    print("Informe del Sistema")
    print("-" * 20)
    print(f"Total personas: {Persona.total_personas}")
    print(f"Total estudiantes: {Estudiante.total_estudiantes}")
    print(f"Total profesores: {Profesor.total_profesores}")
    print("-" * 20)
while True:
    mostrar_menu()
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        registrar_persona()
    elif opcion == 2:
        generar_informe()
        break
    else:
        print("Opción no válida.")
