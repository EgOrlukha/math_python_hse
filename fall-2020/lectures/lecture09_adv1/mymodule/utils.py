def div():
    try:
        x = int(input())
        y = int(input())
        answer = x / y
    except ValueError:
        print('Неверное введенное значение для перевода в целое число!')
        return div()
    except ZeroDivisionError:
        print('Возникло деление на ноль!')
        answer = 0
    return answer

def sum(a, b):
    return a + b

def hello():
    print('Hello world!!!')

constant = 10042