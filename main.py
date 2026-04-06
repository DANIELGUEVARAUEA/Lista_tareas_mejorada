# Importamos tkinter
import tkinter as tk

# Importamos los servicios
from servicios.tarea_servicio import TareaServicio
from servicios.usuario_servicio import UsuarioServicio

# Importamos las interfaces
from ui.login_tkinter import LoginTkinter
from ui.app_tkinter import AppTkinter


# Función principal del programa
def main():
    # Creamos la ventana principal
    root = tk.Tk()

    # Creamos el servicio de usuarios
    usuario_servicio = UsuarioServicio()

    # Creamos el servicio de tareas
    tarea_servicio = TareaServicio()

    # Función interna que abrirá la interfaz principal
    def abrir_sistema():
        AppTkinter(root, tarea_servicio)

    # Primero abrimos la ventana de login
    LoginTkinter(root, usuario_servicio, abrir_sistema)

    # Ejecutamos el ciclo principal de la interfaz
    root.mainloop()


# Verificamos si este archivo se está ejecutando directamente
if __name__ == "__main__":
    main()