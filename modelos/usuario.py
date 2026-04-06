# Clase que representa un usuario del sistema
class Usuario:
    # Constructor de la clase
    def __init__(self, nombre_usuario, contrasena):
        # Atributo privado para guardar el nombre del usuario
        self.__nombre_usuario = nombre_usuario

        # Atributo privado para guardar la contraseña
        self.__contrasena = contrasena

    # Método para obtener el nombre de usuario
    def get_nombre_usuario(self):
        return self.__nombre_usuario

    # Método para obtener la contraseña
    def get_contrasena(self):
        return self.__contrasena

    # Método para convertir el usuario a texto y guardarlo en TXT
    def to_texto(self):
        return f"{self.__nombre_usuario}|{self.__contrasena}"

    # Método estático para crear un objeto Usuario desde una línea del archivo
    @staticmethod
    def from_texto(linea):
        partes = linea.strip().split("|")
        return Usuario(partes[0], partes[1])