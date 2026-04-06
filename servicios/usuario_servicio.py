# Importamos la clase Usuario
from modelos.usuario import Usuario


# Clase que maneja la lógica de registro e inicio de sesión
class UsuarioServicio:
    # Constructor
    def __init__(self, archivo="usuarios.txt"):
        # Archivo donde se guardarán los usuarios
        self.__archivo = archivo

        # Lista privada de usuarios
        self.__usuarios = []

        # Cargamos usuarios existentes
        self.cargar_usuarios()

    # Método para cargar usuarios desde el archivo
    def cargar_usuarios(self):
        try:
            with open(self.__archivo, "r", encoding="utf-8") as archivo:
                self.__usuarios = [
                    Usuario.from_texto(linea)
                    for linea in archivo
                    if linea.strip()
                ]
        except FileNotFoundError:
            # Si no existe el archivo, la lista queda vacía
            self.__usuarios = []

    # Método para guardar los usuarios en el archivo
    def guardar_usuarios(self):
        with open(self.__archivo, "w", encoding="utf-8") as archivo:
            for usuario in self.__usuarios:
                archivo.write(usuario.to_texto() + "\n")

    # Método para registrar un nuevo usuario
    def registrar_usuario(self, nombre_usuario, contrasena):
        # Quitamos espacios innecesarios
        nombre_usuario = nombre_usuario.strip()
        contrasena = contrasena.strip()

        # Validamos que ambos campos tengan información
        if not nombre_usuario or not contrasena:
            return False, "Debe ingresar usuario y contraseña."

        # Revisamos si el usuario ya existe
        for usuario in self.__usuarios:
            if usuario.get_nombre_usuario() == nombre_usuario:
                return False, "El usuario ya existe."

        # Si no existe, lo creamos
        nuevo_usuario = Usuario(nombre_usuario, contrasena)

        # Lo agregamos a la lista
        self.__usuarios.append(nuevo_usuario)

        # Guardamos en el archivo TXT
        self.guardar_usuarios()

        return True, "Usuario registrado correctamente."

    # Método para validar el login
    def validar_login(self, nombre_usuario, contrasena):
        # Recorremos los usuarios registrados
        for usuario in self.__usuarios:
            if (
                usuario.get_nombre_usuario() == nombre_usuario
                and usuario.get_contrasena() == contrasena
            ):
                return True

        return False