from app.notebook import Notebook
from app.console import Console

def main():
    notebook = Notebook()
    console = Console(notebook)

if __name__ == "__main__":
    main()
