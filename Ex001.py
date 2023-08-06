def get_num():
    while True:
        try:
            return float(input('Введите целое или дробное число: '))
        except ValueError as e:
            print('Неверный ввод. Повторите ввод.')


if __name__ == '__main__':
    get_num()
