import json


class UserException(Exception):
    pass


class LevelException(UserException):
    def __init__(self, level_0, level_1):
        self.level_0 = level_0
        self.level_1 = level_1

    def __str__(self):
        return f'Уровень нового пользователя ниже вашего: {self.level_0} < {self.level_1}'


class AccessEception(UserException):
    def __init__(self, name, n_id):
        self.name = name
        self.n_id = n_id

    def __str__(self):
        return f'Вы ввели неверный данные для входа: {self.name} {self.n_id}'


class User():

    def __init__(self, name, n_id, level):
        self.name = name
        self.n_id = n_id
        self.level = level

    def __str__(self):
        return (f'{self.name} {self.n_id} {self.level}')

    def __eq__(self, other):
        return self.name == other.name and self.n_id == other.n_id


class Project():

    def __init__(self, level=-1):
        self.level = level
        self.users = []

    def from_json(self):
        with open('Homework13/level.json', 'r', encoding='utf-8') as data_output:
            level_dic = json.load(data_output)
        for key_0, value_0 in level_dic.items():
            if value_0:
                for key_1, value_1 in value_0.items():
                    temp = User(value_1, key_1, key_0)
                    self.users.append(temp)
        for i in range(len(self.users)):
            print(self.users[i])

    def system_enter(self):
        print('Для входа в систему введите:')
        name = input('Введите имя: ')
        n_id = input('Введите личный идентификатор: ')
        temp = User(name, n_id, -1)
        for i in range(len(self.users)):
            if self.users[i].__eq__(temp):
                self.level = self.users[i].level
                return f'Уровень доступа: {self.users[i].level}'
        raise AccessEception(name, n_id)

    def new_user(self):
        print('Введите данные нового пользователя:')
        name = input('Введите имя: ')
        n_id = input('Введите личный идентификатор: ')
        level = input('Введите уровень доступа: ')
        if level > self.level:
            temp = User(name, n_id, level)
            self.users.append(temp)
            return 'Пользователь успешно добавлен'
        raise LevelException(level, self.level)


if __name__ == '__main__':
    a = Project()
    a.from_json()
    print(a.system_enter())
    print(a.new_user())
