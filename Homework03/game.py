class Game:
    def __init__(self, field):
        self.field = field
        self.player1 = Player(chr(10060), False)
        self.player2 = Player(chr(11093), True)

    def move(self, player, cell):
        self.field.set_item_in_cell(player.item, cell)
        self.field.check_win()
        self.field.check_draw()

    def get_active_player(self):
        self.player1.is_active, self.player2.is_active = self.player2.is_active, self.player1.is_active
        if self.player1.is_active:
            return self.player1
        return self.player2


class Player:
    def __init__(self, item, is_active: bool):
        self.item = item
        self.is_active = is_active
