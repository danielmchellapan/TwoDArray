class TwoDArray:

    def __init__(self):
        self._board = []
        board1 = [[0]*8 for _ in range(8)]
        for x in board1:
            print(x)
            self._board.append(x)


def print_hi():
    TwoDArray()


if __name__ == '__main__':
    print_hi()
