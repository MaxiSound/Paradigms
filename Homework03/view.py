import sys

import exceptions


class View:
    def __init__(self, game):
        self.game = game

    def start_game(self):
        while True:
            self.show_field()
            player = self.game.get_active_player()
            while True:
                try:
                    cell = int(input(f'Ход {player.item}: '))
                    self.game.move(player, cell)
                    break
                except exceptions.EndGameException as ex:
                    print(ex)
                    self.show_field()
                    sys.exit()
                except exceptions.GameException as ex:
                    print(ex)

    def show_field(self):
        print('-' * 9)
        for i in range(0, 9, 3):
            dct = [*self.game.field.cells.items()][i: i + 3]
            print('\t'.join(
                [str(cell[0]) if cell[1].item is None else cell[1].item for cell in dct]))
            print('-' * 9)
