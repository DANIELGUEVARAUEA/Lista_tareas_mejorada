# Importamos la clase Tarea desde la carpeta modelos
from modelos.tarea import Tarea


# Clase que contiene la lógica de negocio para manejar tareas
class TareaServicio:
    # Constructor de la clase
    def __init__(self, archivo="tareas.txt"):
        # Nombre del archivo donde se guardarán las tareas
        self.__archivo = archivo

        # Lista privada que almacenará los objetos Tarea
        self.__tareas = []

        # Al iniciar el programa, cargamos las tareas guardadas
        self.cargar_tareas()

    # Método para agregar una nueva tarea
    def agregar_tarea(self, descripcion):
        # Eliminamos espacios al inicio y final
        descripcion = descripcion.strip()

        # Verificamos que no esté vacía
        if descripcion:
            # Creamos una nueva tarea
            nueva_tarea = Tarea(descripcion)

            # La agregamos a la lista
            self.__tareas.append(nueva_tarea)

            # Guardamos los cambios en el archivo
            self.guardar_tareas()

            return True

        # Si no hay descripción válida, devolvemos False
        return False

    # Método para devolver la lista de tareas
    def obtener_tareas(self):
        return self.__tareas

    # Método para marcar una tarea como completada usando su índice
    def marcar_completada(self, indice):
        # Verificamos que el índice exista en la lista
        if 0 <= indice < len(self.__tareas):
            # Marcamos la tarea como completada
            self.__tareas[indice].marcar_completada()

            # Guardamos cambios en el archivo
            self.guardar_tareas()

            return True

        return False

    # Método para eliminar una tarea de la lista
    def eliminar_tarea(self, indice):
        # Verificamos que el índice exista
        if 0 <= indice < len(self.__tareas):
            # Eliminamos la tarea
            del self.__tareas[indice]

            # Guardamos nuevamente en el archivo
            self.guardar_tareas()

            return True

        return False

    # Método para guardar todas las tareas en el archivo TXT
    def guardar_tareas(self):
        # Abrimos el archivo en modo escritura
        with open(self.__archivo, "w", encoding="utf-8") as archivo:
            # Recorremos todas las tareas
            for tarea in self.__tareas:
                # Guardamos cada tarea en una línea
                archivo.write(tarea.to_texto() + "\n")

    # Método para cargar las tareas desde el archivo TXT
    def cargar_tareas(self):
        try:
            # Abrimos el archivo en modo lectura
            with open(self.__archivo, "r", encoding="utf-8") as archivo:
                # Convertimos cada línea en un objeto Tarea
                self.__tareas = [
                    Tarea.from_texto(linea)
                    for linea in archivo
                    if linea.strip()
                ]
        except FileNotFoundError:
            # Si el archivo no existe, iniciamos con lista vacía
            self.__tareas = []