from game import Game
from field import Field
from view import View

game = Game(Field())
view = View(game)
view.start_game()
