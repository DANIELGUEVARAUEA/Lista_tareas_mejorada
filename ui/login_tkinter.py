# Importamos tkinter para la interfaz gráfica
import tkinter as tk

# Importamos messagebox para mostrar mensajes emergentes
from tkinter import messagebox


# Clase de la ventana de login
class LoginTkinter:
    # Constructor
    def __init__(self, root, usuario_servicio, abrir_sistema_callback):
        # Ventana principal
        self.root = root

        # Servicio de usuarios
        self.usuario_servicio = usuario_servicio

        # Función que abrirá el sistema principal luego del login
        self.abrir_sistema_callback = abrir_sistema_callback

        # Título de la ventana
        self.root.title("Login - Lista de Tareas")

        # Tamaño de la ventana
        self.root.geometry("400x300")

        # Color de fondo de la ventana
        self.root.config(bg="#f4f4f4")

        # Frame principal del login
        self.frame = tk.Frame(self.root, bg="#f4f4f4")
        self.frame.pack(expand=True)

        # Etiqueta del título
        self.label_titulo = tk.Label(
            self.frame,
            text="INICIO DE SESIÓN",
            font=("Arial", 16, "bold"),
            bg="#f4f4f4"
        )
        self.label_titulo.pack(pady=10)

        # Etiqueta del usuario
        self.label_usuario = tk.Label(
            self.frame,
            text="Usuario:",
            bg="#f4f4f4"
        )
        self.label_usuario.pack()

        # Campo para escribir el usuario
        self.entry_usuario = tk.Entry(self.frame, width=30)
        self.entry_usuario.pack(pady=5)

        # Etiqueta de contraseña
        self.label_contrasena = tk.Label(
            self.frame,
            text="Contraseña:",
            bg="#f4f4f4"
        )
        self.label_contrasena.pack()

        # Campo para escribir la contraseña
        self.entry_contrasena = tk.Entry(self.frame, width=30, show="*")
        self.entry_contrasena.pack(pady=5)

        # Botón para iniciar sesión
        self.boton_login = tk.Button(
            self.frame,
            text="Ingresar",
            bg="#4CAF50",
            fg="white",
            width=20,
            command=self.login
        )
        self.boton_login.pack(pady=5)

        # Botón para registrar usuario
        self.boton_registrar = tk.Button(
            self.frame,
            text="Registrar Usuario",
            bg="#2196F3",
            fg="white",
            width=20,
            command=self.registrar
        )
        self.boton_registrar.pack(pady=5)

        # Botón para salir
        self.boton_salir = tk.Button(
            self.frame,
            text="Salir",
            bg="#f44336",
            fg="white",
            width=20,
            command=self.root.quit
        )
        self.boton_salir.pack(pady=5)

        # Evento de teclado: Enter para login
        self.root.bind("<Return>", lambda event: self.login())

        # Evento de teclado: Escape para salir
        self.root.bind("<Escape>", lambda event: self.root.quit())

    # Método para iniciar sesión
    def login(self):
        # Obtenemos los datos escritos
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()

        # Validamos si existe el usuario
        if self.usuario_servicio.validar_login(usuario, contrasena):
            messagebox.showinfo("Éxito", "Inicio de sesión correcto.")

            # Destruimos el frame del login
            self.frame.destroy()

            # Abrimos el sistema principal
            self.abrir_sistema_callback()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    # Método para registrar usuario
    def registrar(self):
        # Obtenemos datos de los campos
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()

        # Llamamos al servicio
        exito, mensaje = self.usuario_servicio.registrar_usuario(usuario, contrasena)

        # Mostramos resultado
        if exito:
            messagebox.showinfo("Éxito", mensaje)

            # Limpiamos los campos
            self.entry_usuario.delete(0, tk.END)
            self.entry_contrasena.delete(0, tk.END)
        else:
            messagebox.showwarning("Atención", mensaje)