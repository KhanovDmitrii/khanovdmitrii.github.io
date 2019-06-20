def wrap(func):
    def write(*args, **kwargs):
        res = func(*args, **kwargs)
        with open('istroriya', 'a') as f:
            stri = args[3].get(str(args[2])) + ': ' + str(args[0]) + ' ' + str(args[2]) + ' ' + str(args[1]) + ' = ' + str(res)
            f.write(stri)
            f.write('\r\n')
        return res
    return write

@wrap
def calc(op1, op2, action, d):
     return eval(f"{op1} {action} {op2}")

d = {'*' : 'умножение', '/' : 'деление', '+' : 'плюс', '-' : 'минус'}

a = ''
print('Для выхода из программы нажмите exit')
while(a != 'exit'):
    a = input('Введите первое число:')
    if(a != 'exit'):
        b = input('Введите второе число')
        d_c = input('Введите операцию:')
        calc(int(a), int(b), d_c, d)
