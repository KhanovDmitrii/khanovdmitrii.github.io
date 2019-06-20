def wrap(func):
    def write(*args, **kwargs):
        res = func(*args, **kwargs)
        with open('istroriya_1', 'a') as f:
            stri = args[3].get(str(args[2])) + ': ' + str(args[0]) + ' ' + str(args[2]) + ' ' + str(args[1]) + ' = ' + str(res)
            f.write(stri)
            f.write('\r\n')
        return res
    return write

def calc(op1, op2, action, d):
     return eval(f"{op1} {action} {op2}")

d = {'*' : 'умножение', '/' : 'деление', '+' : 'плюс', '-' : 'минус'}


f = wrap(calc)
print(f)
a = f('1', '4', '*', d)
print(a)
