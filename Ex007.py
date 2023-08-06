class SquareException(Exception):
    def __init__(self, len):
        self.len = len

    def __str__(self):
        return f'Сторона прямоугольника не может быть отрицательной ({self.len})'


class NumException(Exception):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f'Необходимо ввести число! ({self.num})'


class Square ():

    def __init__(self, len_a=0, len_b=0):
        self._len_a = len_a
        self._len_b = len_b

    def square_length(self):
        print(round(2*self._len_a + 2*self._len_b, 2))

    def square_area(self):
        print(round(self._len_a*self._len_b, 2))

    @property
    def len_a(self):
        return self._len_a

    @property
    def len_b(self):
        return self._len_b

    @len_a.setter
    def len_a(self, len_a):
        if len_a > 0:
            self._len_a = len_a
        else:
            raise SquareException(len_a)

    @len_b.setter
    def len_b(self, len_b):
        if len_b > 0:
            self._len_b = len_b
        else:
            raise SquareException(len_b)


def guess(answer, attempts):
    def guessing_game():
        for _ in range(attempts):
            data = input('Введите число: ')
            try:
                data = int(data)
            except:
                raise NumException(data)
            if data == answer:
                print('Число угадано!')
                return
            elif data < answer:
                print('Больше!')
            else:
                print('Меньше!')
        print('Вы проиграли!')
    return guessing_game


if __name__ == '__main__':
    a = Square(10, 15)
    a.len_a = 10
    game = guess(50, 10)
    game()
