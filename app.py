import os

# Ruta del archivo donde se guardarán las tareas
FILE_PATH = "tasks.txt"

# Función para cargar las tareas desde el archivo
def load_tasks():
    tasks = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

# Función para guardar las tareas en el archivo
def save_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

# Función para agregar una tarea
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Tarea '{task}' agregada.")

# Función para eliminar una tarea
def delete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Tarea '{removed_task}' eliminada.")
    else:
        print("Índice no válido.")

# Función para mostrar todas las tareas
def show_tasks():
    tasks = load_tasks()
    if tasks:
        print("Lista de tareas:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tienes tareas.")

# Función principal que maneja el menú
def main():
    while True:
        print("\n--- Menú de Tareas ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        option = input("Seleccione una opción: ")

        if option == "1":
            show_tasks()
        elif option == "2":
            task = input("Ingrese la nueva tarea: ")
            add_task(task)
        elif option == "3":
            show_tasks()
            try:
                task_index = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
                delete_task(task_index)
            except ValueError:
                print("Por favor ingrese un número válido.")
        elif option == "4":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

# Ejecutar la función principal si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()
