from tkinter import Tk, Menu, messagebox, simpledialog, Frame
from tkinter import ttk
import pandas as pd

# Ruta del archivo de Excel
nombreArchivo = "/home/b5/Descargas/pueba.xls"
# Cargar el archivo de Excel
estudiantes = pd.read_excel(nombreArchivo)

class MenuApp:
    def __init__(self, master):
        self.master = master
        self.create_menu()
        
        # Crear un frame para mostrar los datos
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)

    def create_menu(self):
        # Crear la barra de menú
        barra_menus = Menu(self.master)

        # Crear el menú "Excel"
        menu_excel = Menu(barra_menus, tearoff=0)
        barra_menus.add_cascade(label="Excel", menu=menu_excel)
        menu_calculos = Menu(barra_menus, tearoff=0)
        barra_menus.add_cascade(label="Cálculos", menu=menu_calculos)

        # Agregar opciones al menú "Excel"
        menu_excel.add_command(label="Todos", command=self.show_all)
        menu_excel.add_command(label="Nombre", command=self.show_name)
        menu_excel.add_command(label="Mayores de 18", command=self.show_over_18)
        
        menu_calculos.add_command(label="Promedio", command=self.promedio)
        menu_calculos.add_command(label="Mediana", command=self.mediana)
        menu_calculos.add_command(label="Moda", command=self.moda)

        # Configurar la barra de menú en la ventana principal
        self.master.config(menu=barra_menus)

    def show_all(self):
        # Limpiar la ventana anterior
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Crear un Treeview para mostrar los datos
        tree = ttk.Treeview(self.frame)

        # Definir columnas
        tree['columns'] = list(estudiantes.columns)
        tree['show'] = 'headings'  # Mostrar solo las cabeceras

        # Configurar encabezados
        for column in tree['columns']:
            tree.heading(column, text=column)

        # Agregar datos al Treeview
        for index, row in estudiantes.iterrows():
            tree.insert("", "end", values=list(row))

        tree.pack(fill="both", expand=True)
        
    def promedio(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        promedio_edad = estudiantes["edad"].mean()
        
        messagebox.showinfo("El promedio es", f"El promedio de la edad es: {promedio_edad: }")
        
        
    def mediana (self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        medianaa = estudiantes["edad"].median()
    
        messagebox.showinfo("La mediana es", f"La mediana de la edad es: {medianaa}")
        
    def moda (self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        modaa = estudiantes["edad"].mode()
    
        messagebox.showinfo("La moda es", f"La moda de la edad es: {modaa}")

    def show_name(self):
        name = simpledialog.askstring("Nombre", "Introduce tu nombre:")
        if name:
            messagebox.showinfo("Nombre ingresado", f"Tu nombre es: {name}")

    def show_over_18(self):
       # Limpiar el frame anterior
        for widget in self.frame.winfo_children():
            widget.destroy()

    # Filtrar estudiantes mayores de 18
        mayores_de_18 = estudiantes[estudiantes['edad'] >= 18]

    # Crear un Treeview para mostrar los datos filtrados
        tree = ttk.Treeview(self.frame)
        tree['columns'] = list(mayores_de_18.columns)
        tree['show'] = 'headings'

    # Configurar encabezados
        for column in tree['columns']:
            tree.heading(column, text=column)

    # Agregar datos al Treeview
        for index, row in mayores_de_18.iterrows():
            tree.insert("", "end", values=list(row))
    
            tree.pack(fill="both", expand=True)

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Aplicación con Menú Excel")
        
        # Establecer el tamaño de la ventana (ancho x alto)
        self.root.geometry("800x200")  # Cambia estos valores a tu gusto
        
        # Crear el menú
        self.menu_app = MenuApp(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()

