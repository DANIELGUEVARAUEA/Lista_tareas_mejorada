# Importamos tkinter
import tkinter as tk

# Importamos messagebox para mostrar mensajes
from tkinter import messagebox


# Clase de la interfaz principal del sistema
class AppTkinter:
    # Constructor
    def __init__(self, root, servicio):
        # Ventana principal
        self.root = root

        # Servicio que maneja la lógica de tareas
        self.servicio = servicio

        # Configuración de la ventana
        self.root.title("Lista de Tareas")
        self.root.geometry("520x620")
        self.root.config(bg="#e8f0fe")

        # Frame principal
        self.frame_principal = tk.Frame(self.root, bg="#e8f0fe")
        self.frame_principal.pack(pady=20)

        # Título de la aplicación
        self.label_titulo = tk.Label(
            self.frame_principal,
            text="GESTOR DE TAREAS",
            font=("Arial", 18, "bold"),
            bg="#e8f0fe"
        )
        self.label_titulo.pack(pady=10)

        # Campo de entrada para escribir tareas
        self.entry_tarea = tk.Entry(
            self.frame_principal,
            width=40,
            font=("Arial", 12)
        )
        self.entry_tarea.pack(pady=10)

        # Listbox para mostrar las tareas
        self.lista_tareas = tk.Listbox(
            self.frame_principal,
            width=45,
            height=12,
            font=("Arial", 11)
        )
        self.lista_tareas.pack(pady=10)

        # Botón para agregar tarea
        self.boton_agregar = tk.Button(
            self.frame_principal,
            text="Añadir Tarea",
            bg="#4CAF50",
            fg="white",
            width=20,
            command=self.agregar_tarea
        )
        self.boton_agregar.pack(pady=5)

        # Botón para marcar tarea como completada
        self.boton_completar = tk.Button(
            self.frame_principal,
            text="Marcar Completada",
            bg="#2196F3",
            fg="white",
            width=20,
            command=self.marcar_completada
        )
        self.boton_completar.pack(pady=5)

        # Botón para eliminar tarea
        self.boton_eliminar = tk.Button(
            self.frame_principal,
            text="Eliminar Tarea",
            bg="#f44336",
            fg="white",
            width=20,
            command=self.eliminar_tarea
        )
        self.boton_eliminar.pack(pady=5)

        # Botón para limpiar el campo
        self.boton_limpiar = tk.Button(
            self.frame_principal,
            text="Limpiar Campo",
            bg="#FF9800",
            fg="white",
            width=20,
            command=self.limpiar_campo
        )
        self.boton_limpiar.pack(pady=5)

        # Frame inferior para las instrucciones
        self.frame_instrucciones = tk.Frame(self.root, bg="#d9e2f2")
        self.frame_instrucciones.pack(side="bottom", fill="x")

        # Etiqueta de instrucciones
        self.label_instrucciones = tk.Label(
            self.frame_instrucciones,
            text="Teclas rápidas: C = completar tarea | D = eliminar tarea | Esc = salir",
            font=("Arial", 10, "bold"),
            bg="#d9e2f2",
            fg="black",
            pady=10
        )
        self.label_instrucciones.pack()

        # Evento de teclado: Enter agrega tarea
        self.root.bind("<Return>", lambda event: self.agregar_tarea())

        # Evento de teclado: tecla C solo en la lista
        self.lista_tareas.bind("<c>", lambda event: self.marcar_completada())
        self.lista_tareas.bind("<C>", lambda event: self.marcar_completada())

        # Evento de teclado: tecla D solo en la lista
        self.lista_tareas.bind("<d>", lambda event: self.eliminar_tarea())
        self.lista_tareas.bind("<D>", lambda event: self.eliminar_tarea())

        # Evento de teclado: Escape cierra la aplicación
        self.root.bind("<Escape>", lambda event: self.root.quit())

        # Cuando el usuario seleccione una tarea, la lista toma el foco
        self.lista_tareas.bind("<<ListboxSelect>>", self.enfocar_lista)

        # También cuando haga clic con el mouse
        self.lista_tareas.bind("<Button-1>", self.enfocar_lista)

        # Cargamos la lista visual al iniciar
        self.actualizar_lista()

        # Foco inicial en el campo de texto
        self.entry_tarea.focus_set()

    # Método para dar foco a la lista
    def enfocar_lista(self, event=None):
        self.lista_tareas.focus_set()

    # Método para agregar tarea
    def agregar_tarea(self):
        descripcion = self.entry_tarea.get()

        if self.servicio.agregar_tarea(descripcion):
            self.entry_tarea.delete(0, tk.END)
            self.actualizar_lista()
            self.entry_tarea.focus_set()
        else:
            messagebox.showwarning("Atención", "Ingrese una tarea válida.")

    # Método para marcar una tarea como completada
    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()

        if seleccion:
            indice = seleccion[0]
            self.servicio.marcar_completada(indice)
            self.actualizar_lista()

            if indice < self.lista_tareas.size():
                self.lista_tareas.selection_set(indice)
                self.lista_tareas.focus_set()
        else:
            messagebox.showwarning("Atención", "Seleccione una tarea.")

    # Método para eliminar una tarea
    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()

        if seleccion:
            indice = seleccion[0]
            self.servicio.eliminar_tarea(indice)
            self.actualizar_lista()

            if self.lista_tareas.size() > 0:
                nuevo_indice = min(indice, self.lista_tareas.size() - 1)
                self.lista_tareas.selection_set(nuevo_indice)
                self.lista_tareas.focus_set()
            else:
                self.entry_tarea.focus_set()
        else:
            messagebox.showwarning("Atención", "Seleccione una tarea para eliminar.")

    # Método para limpiar el campo
    def limpiar_campo(self):
        self.entry_tarea.delete(0, tk.END)
        self.entry_tarea.focus_set()

    # Método para actualizar la lista visual
    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)

        for tarea in self.servicio.obtener_tareas():
            if tarea.esta_completada():
                texto = f"✔ {tarea.get_descripcion()}"
            else:
                texto = f"✘ {tarea.get_descripcion()}"

            self.lista_tareas.insert(tk.END, texto)

        for i, tarea in enumerate(self.servicio.obtener_tareas()):
            if tarea.esta_completada():
                self.lista_tareas.itemconfig(i, fg="green")
            else:
                self.lista_tareas.itemconfig(i, fg="red")