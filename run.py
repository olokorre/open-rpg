from models.world import World
from models.game_ui.interface import Interface

world = World(
    heigth=320,
    width=320
)
ui = Interface(
    world=world
)

if __name__ == '__main__':
    ui.main()