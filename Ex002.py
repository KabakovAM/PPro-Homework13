def get_dic(dic, key, res):
    while True:
        try:
            return dic[key]
        except KeyError as e:
            print('Ключ отсутствует.')
            return res


if __name__ == '__main__':
    dic = {'a': 0, 'b': 1, 'c': 2}
    print(get_dic(dic, 'd', -1))
