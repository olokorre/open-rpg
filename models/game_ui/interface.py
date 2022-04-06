from .setup import Setup

class Interface(Setup):
    def __init__(self, world):
        super().__init__()
        self.world = world
    
    def descrever_command(self):
        print(self.world.getMap())

    def excute_command(self, command):
        if command == 'exit': exit()
        elif command == 'help': self.help_command()
        elif command == 'descrever': self.descrever_command()

    def main(self):
        while True:
            command = input('> ')
            if self.validate_command(command):
                self.excute_command(command)