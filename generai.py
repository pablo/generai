# plugins
from yapsy.PluginManager import PluginManager

def list_plugins():
    print("TO DO")

def start_game():
    print("TO DO")

def do_quit():
    quit()

def menu():
    for option in options:
        print(option["description"])

options = [
    {
        "val": "1",
        "description": "1. Listar Plugins",
        "fn": list_plugins
    },
    {
        "val": "2",
        "description": "2. Jugar",
        "fn": start_game
    },
    {
        "val": ["q", "Q"],
        "description": "Q. Salir",
        "fn": do_quit
    }
]

def process_option(opt):
    for option in options:
        if (isinstance(option["val"], list) and opt in option["val"]) or (opt == option["val"]):
            option["fn"]()

if __name__ == "__main__":
    while True:
        menu()
        opt = input("? ")
        process_option(opt)
