import json
import pytest


def fileopen(name):
    try:
        with open(name, 'r') as fio:
            return fio.read()
    except(IOError, Exception) as e:
        print(e)
        return None


def read_json(text):
    try:
        return json.loads(text)
    except(json.JSONDecodeError, Exception) as e:
        print(e)
        return None


filepath = 'json.json'
fl = fileopen(filepath)

text = read_json(fl)
tag = dict.keys(text[0])
d = int(len(text[3].get('email')))
print('|index: ', end='')
[print(text[s].get('index'), end=' '*(d - len(str(text[s].get('index')))) +'|') for s in range(0, len(text))]
print()
print('|age:   ', end='')
[print(text[s].get('age'), end=' '*(d - len(str(text[s].get('age')))) +'|') for s in range(0, len(text))]
print()
print('|name:  ', end='')
[print(str(text[s].get('name').get('first')) + ' ' + str(text[s].get('name').get('last')), end=' '*(d - len(str(str(text[s].get('name').get('first'))
                                   + ' ' + str(text[s].get('name').get('last'))))) +'|') for s in range(0, len(text))]
print()
print('|email: ', end='')
[print(text[s].get('email'), end=' '*(d - len(str(text[s].get('email')))) +'|') for s in range(0, len(text))]
print()
print('|phone: ', end='')
[print(text[s].get('phone'), end=' '*(d - len(str(text[s].get('phone')))) +'|') for s in range(0, len(text))]


if __name__ == '__main__':

    def test_fileopen():
        assert fileopen('qweqwe') is None


    def test_read_json():
        assert read_json('1||]') is None

