class Setup(object):
    def __init__(self):
        self.allowed_commands = [
            'ajuda',
            'descrever',
            'sair'
        ]
        self.commands_descriptions = {
            'ajuda': 'Mostrar essa página',
            'descrever': 'Perguntar ao mestre o que à nos',
            'sair': 'Sair do jogo'
        }

    def help_command(self):
        print('Comando permitidos:')
        for command in self.allowed_commands:
            print(command + ': ' + self.commands_descriptions[command])

    def validate_command(self, command):
        if command not in self.allowed_commands:
            print('Comando inválido!')
            return False
        return True