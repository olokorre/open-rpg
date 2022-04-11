from .setup import Setup
from ..player import Player

class Interface(Setup):
    def __init__(self, world):
        super().__init__()
        self.world = world
    
    def descrever_command(self):
        print(self.world.getMap())

    def excute_command(self, command):
        if command == 'sair': exit()
        elif command == 'ajuda': self.help_command()
        elif command == 'descrever': self.descrever_command()

    def init_game(self):
        print('Primeira vez?\nCrie seu personagem!')
        nickname = input('Nome: ')
        return Player(nickname)

    def main(self):
        self.world.setPlayer(self.init_game())
        while True:
            command = input('[%s@open-rpg]$ '%self.world.player.getNickname())
            if self.validate_command(command):
                self.excute_command(command)