class TwoDArray:

    def __init__(self):
        self._array = []
        temp_array = [1, 2, 3, 4, 5, 6, 7, 8]
        for i in temp_array:
            self._array.append(i)
        print(self._array)


def print_hi():
    TwoDArray()


if __name__ == '__main__':
    print_hi()
