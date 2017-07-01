# coding=utf-8
from os import listdir
from os.path import isfile, join
from importlib import import_module
from game import Game
from sandboxing import getName
# plugins

plugins = {}
plugins_list=[]
def load_plugins():
    print("Loading plugins...")
    plugin_files = [f for f in listdir('plugins') if isfile(join('plugins',
        f)) and f.endswith('.py') and f != "__init__.py"]
    plugins_loaded = 0
    invalid_plugins = 0
    for plugin_file in plugin_files:
        plugin_name = plugin_file[:-3]
        print("Loading plugin {0}".format(plugin_name))
        try:
            name = getName(plugin_file)
            if(name is not None):
                plugins_loaded = plugins_loaded + 1
                plugins[name] = plugin_file
                plugins_list.append(name)
            else:
                raise Exception(name)
        except Exception as e:
            print("Plugin {0} was not loaded {1}".format(plugin_name, e))
            invalid_plugins = invalid_plugins + 1
    print("Plugins loaded: {0}\nInvalid plugins: {1}".format(plugins_loaded, invalid_plugins))

def list_plugins(title=True):
    if title:
        print("---------------- PLUGINS -----------------")
    i = 0
    for plugin in plugins_list:
        print("{0}) {1}".format(i, plugin))
        i = i + 1
    print("\n")

def start_game():
    print("---------------- GENERALA -----------------")
    list_plugins(False)

    players_input = raw_input("Ingrese los jugadores (separándolos con ,): ")
    players = [int(x.strip()) for x in players_input.split(",")]
    nscoresheets = int(raw_input("Cuántas casillas? "))
    game = Game(nscoresheets)
    for player in players:
        game.add_player(plugins_list[player],plugins[plugins_list[player]])
    game.start()
    game.results()


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
        if (isinstance(option["val"], list) and opt in option["val"]) or (str(opt) == option["val"]):
            option["fn"]()

if __name__ == "__main__":
    load_plugins()
    while True:
        menu()
        opt = input("? ")
        process_option(opt)
