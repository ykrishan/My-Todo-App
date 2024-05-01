FILEPATH ="Todos.txt"

"""read file function Which store in Todos.txt"""
def get_Todos(filepath = FILEPATH):
    with open(filepath, 'r') as file:
        Todos = file.readlines()
    return Todos

def write_Todos(Todos_Arg, filepath = FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(Todos_Arg)

if __name__ == "__main__":
    print(get_Todos())
