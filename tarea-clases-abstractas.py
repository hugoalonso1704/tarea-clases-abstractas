from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def presentarse(self):
        pass

    @abstractmethod
    def actividad_diaria(self):
        pass

    def cumplir_anios(self):
        self.edad += 1
        return f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años."

class Alumno(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estoy en {self.curso}."

    def actividad_diaria(self):
        return f"{self.nombre} va a clase, toma apuntes y hace los deberes de {self.curso}."

class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def presentarse(self):
        return f"Buenos días, soy {self.nombre}, profesor de {self.asignatura}."

    def actividad_diaria(self):
        return f"{self.nombre} prepara y da clases de {self.asignatura} y corrige exámenes."


if __name__ == "__main__":
    alumno = Alumno("Lucía", 15, "4º de ESO")
    profesor = Profesor("Carlos", 42, "Matemáticas")

    for persona in (alumno, profesor):
        print(persona.presentarse())
        print(persona.actividad_diaria())
        print(persona.cumplir_anios())
        print()

    try:
        pepe = Persona("Pepe", 30)
    except TypeError as error:
        print("No se puede crear una Persona directamente:")
        print(error)
        