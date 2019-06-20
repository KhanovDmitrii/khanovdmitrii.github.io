import json
import csv


def json_writer(text, src):
    try:
        json.loads(text)
        print(json.dumps(text))
    except(json.JSONDecodeError, Exception) as e:
        print(e)
        raise ValueError
    else:
        try:
            with open(src, 'w') as outfile:
                json.dump(text, outfile)
        except(IOError, Exception) as e:
            print(e)
            raise IOError


def csv_writer(text, src):
    try:
        csv.reader(text)
    except(csv.Error, Exception) as e:
        print(e)
        raise ValueError
    else:
        try:
            with open(src, "w", newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                for line in text:
                    writer.writerow(line)
        except(IOError, Exception) as e:
            print(e)
            raise IOError


user_pref = input('Сохранить строку в JSON или в CSV?')
print(user_pref)
print('Введите exit когда закончите вводить данные')
key = ''
user_input = ''
while key != 'exit':
    key = input()
    if key != 'exit':
        user_input += key + '\n'

print('Выввели: ' + user_input)
user_source = input('Введите путь и имя файла, куда вы хотите сохранить')

if(user_pref == 'JSON') or (user_pref == str(1)):
    json_writer(user_input, str(user_source))
elif(user_pref == 'CSV') or (user_pref == str(2)):
    csv_writer(user_input, str(user_source))
