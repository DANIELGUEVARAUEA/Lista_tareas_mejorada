# Clase que representa una tarea del sistema
class Tarea:
    # Constructor de la clase
    def __init__(self, descripcion, completada=False):
        # Atributo privado para guardar la descripción de la tarea
        self.__descripcion = descripcion

        # Atributo privado para saber si la tarea está completada o no
        self.__completada = completada

    # Método para obtener la descripción
    def get_descripcion(self):
        return self.__descripcion

    # Método para cambiar la descripción
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    # Método para consultar si la tarea está completada
    def esta_completada(self):
        return self.__completada

    # Método para marcar la tarea como completada
    def marcar_completada(self):
        self.__completada = True

    # Método para marcar la tarea como pendiente
    def marcar_pendiente(self):
        self.__completada = False

    # Método para convertir el objeto en texto y guardarlo en un archivo TXT
    def to_texto(self):
        return f"{self.__descripcion}|{self.__completada}"

    # Método estático para reconstruir una tarea desde una línea de texto
    @staticmethod
    def from_texto(linea):
        partes = linea.strip().split("|")
        descripcion = partes[0]
        completada = partes[1] == "True"
        return Tarea(descripcion, completada)