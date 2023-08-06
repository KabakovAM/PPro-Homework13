import json


class User():

    def __init__(self, name, n_id, level):
        self.name = name
        self.n_id = n_id
        self.level = level

    def __str__(self):
        return (f'{self.name} {self.n_id} {self.level}')


def from_json():
    users = []
    with open('Homework13/level.json', 'r', encoding='utf-8') as data_output:
        level_dic = json.load(data_output)
    for key_0, value_0 in level_dic.items():
        if value_0:
            for key_1, value_1 in value_0.items():
                temp = User(value_1, key_1, key_0)
                users.append(temp)
    for i in range(len(users)):
        print(users[i])


if __name__ == '__main__':
    from_json()
