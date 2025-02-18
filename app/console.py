from app.notebook import Notebook

class Console:

    def __init__ (self, notebook: Notebook):
        self.notebook = Notebook

    def display_menu (self):
        print("\nMenú:")
        print("1. Agregar nota")
        print("2. Listar notas")
        print("3. Agregar etiqueta a nota")
        print("4. Listar notas importantes")
        print("5. Eliminar nota")
        print("6. Mostrar notas por etiqueta")
        print("7. Mostrar etiqueta con más notas")
        print("8. Salir")
