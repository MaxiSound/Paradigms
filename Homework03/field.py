import exceptions


class Field:
    def __init__(self):
        self.cells = {i: Cell() for i in range(1, 10)}

    def set_item_in_cell(self, item, cell):
        cell = self._get_cell(cell)
        cell.set_item(item)

    def _get_cell(self, i):
        cell = self.cells.get(i)
        if cell is None:
            raise exceptions.GameException('Такой ячейки не существует')
        return cell

    def check_win(self):
        win_routes = (1, 2, 3), (4, 5, 6), (7, 8, 9), \
            (1, 4, 7), (2, 5, 8), (4, 5, 6), \
            (7, 5, 3), (1, 5, 9)
        for route in win_routes:
            cell = self.cells[route[0]]
            for i in route:
                if cell.item is None or self.cells[i].item != cell.item:
                    break
            else:
                raise exceptions.EndGameException(f'Победа! {cell.item}!')

    def check_draw(self):
        for cell in self.cells.values():
            if cell.item is None:
                break
        else:
            raise exceptions.EndGameException(f'Ничья!')


class Cell:
    def __init__(self):
        self.item = None

    def set_item(self, item):
        if self.item:
            raise exceptions.GameException('Эта ячейка уже используется')
        self.item = item
