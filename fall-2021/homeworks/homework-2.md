# Домашнее задание #2: Класс многочленов [черновик]

Реализация класса многочленов [сдается в контест](https://contest.yandex.ru/contest/29819/enter).

Код для code-review [сдается в Replit](https://replit.com/@HSE-Math-Python/Polynom). Не забудьте нажать кнопку Submit, когда будете готовы сдать задание.

## Класс многочленов

В этой задаче вам нужно реализовать класс `Polynomial` для работы с многочленами. Методы, которые будут проверяться в задаче уже определены в шаблоне ниже и в Replit шаблоне. Вам не запрещается добавлять свои функции, переменные или методы, однако запрещается менять названия предоставленных методов. Разрешается использовать только стандартную библиотеку Python. 

**Совет #1:** заранее подумайте, какую структуру данных использовать для хранения коэффициентов.

**Совет #2:** продумайте реализацию метода `__str__`, при грамотном подходе код метода должен занимать не более 30 строчек.

**Важно:** в Яндекс.Контесте в качестве компилятор стоит Питон версии 3.5 (в силу другой структуры проверки кода), поэтому, например, нет возможности использовать f-string. Кроме того стоит проверка на PEP, советуем сразу писать красивый код или в дальнейшем пользоваться автоисправлением ([например](https://www.tutorialspoint.com/online_python_formatter.htm))

Правила оценивания:

- За прохождение открытых тестов (есть файл ниже) ставится 4 балла.
- За прохождение приватных тестов ставится еще от 0 до 5 баллов.
- Для получения оценки 10 необходимо также реализовать метод подсчета НОД многочленов (тест в контесте появится в ближайшее время).
- За code review возможно снижение оценки на 30% и менее.

## Требования к реализации

1) Конструктор `__init__` позволяет построить многочлен
    - по списку коэффициентов, в котором первым идет свободный член

        ```python
        In[1] : print(Polynomial([1, 2, 3]))
        Out[1]: 3x^2 + 2x + 1
        ```

    - по словарю вида `{степень: коэффициент}`

        ```python
        In[2] : print(Polynomial({0:-3, 2:1, 5:4}))
        Out[2]: 4x^5 + x^2 - 3
        ```

    - по другому многочлену

        ```python
        In[3] : poly = Polynomial({0:-3, 2:1, 5:4})
           ...: poly_copy = Polynomial(poly)
        ```

    - по набору коэффициентов, в котором первым идет свободной член

        ```python
        In[4] : print(Polynomial(0, 2, 0, 5))
        Out[4]: 5x^3 + 2x
        ```

    **Примечания:**

    - Для корректной работы `print` нужно перегрузить `__str__` определенный ниже
    - Для сравнения типов используйте `[isinstance](https://pythoner.name/isinstance-type)`
    - Создание функции с переменным количеством аргументов

        ```python
        In[5] : def func(*args):
        ...       return args

        In[6] : func(1, 2, 3, 'abc')
        Out[6]:	(1, 2, 3, 'abc')
        ```

        Как видно из примера, args - это кортеж из всех переданных аргументов функции, и с переменной можно работать так же, как и с кортежем.

2) Перегруженный метод `__repr__`, который будет возвращать строку вида: `Polynomial <список коэффициентов>`

    ```python
    In[10] : Polynomial(1, 2, 3, 0, 0, 0, 5, 0, 0)
    Out[10]: Polynomial [1, 2, 3, 0, 0, 0, 5]

    In[11] : repr(Polynomial(2, 3))
    Out[11]: Polynomial [2, 3]
    ```

    **Примечание:**

    - [Difference between str and repr?](https://stackoverflow.com/questions/1436703/difference-between-str-and-repr)

3) Перегруженный метод `__str__`, возвращающий строковое представление объекта. Многочлен должен выводиться начиная от старшей степени. Должны быть приведены подобные, отсутствовать нулевые коэффициенты, а также не должно быть единичных коэффициентов и степеней. Примеры:

    ```python
    In[7] : print(Polynomial(0, 2, 0, 5))
    Out[7]: 5x^3 + 2x

    In[8] : print(Polynomial([7, -2, 0, 1]))
    Out[8]: x^3 - 2x + 7

    In[9] : print(Polynomial([7, -2, 0, -1]))
    Out[9]: -x^3 - 2x + 7
    ```

4) Перегруженные операторы `+, - (в том числе унарный)`. Также должны поддерживаться арифметические операции с числами.
5) Перегруженный оператор `==` для сравнение многочленов на равенство между собой и с числами
6) Метод `degree` возвращающий степень многочлена

    ```python
    In[13] : poly = Polynomial(1, 2, 3)
        ...: print(poly.degree())
    Out[13]: 2
    ```

7) Метод `der(self, d=1)` который вычисляет производную степени `d`
8) Перегруженный оператор `__call__` позволяющий вычислить значение многочлена в точке

    ```python
    In[12] : poly = Polynomial(1, 2, 3)
        ...: print(poly(1))
    Out[12]: 6
    ```

9) Перегруженный оператор `*`, в том числе и для умножения на числа.
10) Перегруженные методы `__iter__` и `__next__` позволяющие проитерироваться по многочлену. На каждом шаге итерации должна возвращаться пара вида `(степень, коэффициент)`

    ```python
    In [3]: for i in p:
       ...:     print(i)
       ...:
    (0, 1)
    (1, 2)
    (2, 3)
    ```

    **Примечание:**

    - [Подробнее про итераторы](https://www.programiz.com/python-programming/iterator)
    
11) Производный класс `RealPolynomial`
    - Данный класс является многочленом нечетной степени от вещественных коэффициентов
    - Создайте ошибку `NotOddDegreeException` и бросайте ее в случае, когда пытаются создать полином `RealPolynomial` четной степени
    - Необходимо реализовать метод `find_root`, возвращающий корень многочлена с точностью заданной точностью `eps`.
12) Производный класс `QuadraticPolynomial`
    - Данный класс является многочленом степени не выше 2
    - Создайте ошибку `DegreeIsTooBigException` и бросайте ее в случае, когда пытаются создать полином `QuadraticPolynomial` степени больше 2
    - Необходимо реализовать метод `solve`, возвращающий список содержащий действительные корни многочлена (соответственно, размер списка равен либо 0, либо 1, либо 2)

### Тестирование

- В Replit можно запустить тестирование на открытых тестов вашего кода:
    - Чтобы тестировать ваш класс в replit, необходимо открыть справа окно Shell, ввести `pip install -U pytest`
    - После установки, для тестирования достаточно выполнить в Shell команду `pytest`
- Локально, создайте файл, содержащий реализацию, с названем `polynomial.py`
- Положите файл с тестами под названием `test_polynomial.py` в ту же папку, где лежит `polynomial.py`.
- Можете закомментировать те части тестов, которые вы еще не реализовали
- Запуск тестов:
    - PyCharm
        - Установка `pytest`
            - Через терминал в PyCharm:
            выполните в терминале `pip install -U pytest`
            - Через настройки PyCharm:
            перейдите в `Settings/Preferences -> Project -> Project Interpreter`. Далее нажмите `+` в левом нижнем углу. Найдите в поиске `pytest`. Нажмите `Install Package`.
        - Далее следуйте инструкциям `[Enable Pytest for your project](https://www.jetbrains.com/help/pycharm/pytest.html#enable-pytest)` и `[Run a test](https://www.jetbrains.com/help/pycharm/pytest.html#run-pytest-test)`
    - MacOS/Linux
        - Установка `pytest`: выполните в терминале `pip install -U pytest`
        - Из папки, где у вас лежат `polynomial.py` и `test_polynomial.py` выполните в терминале `pytest`
- Контест содержит все тесты из файла прикрепленного ниже, а также дополнительные приватные тесты.

### Starter code

Чтобы все корректно работало, не меняйте названия файлов или если вы их просто копируете, то создавайте у себя файлы с названиями указанными ниже.

- `polynomial.py`

    ```python
    # polynomial.py

class Polynomial:

    def __init__(self, *coefficients):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __neg__(self):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __call__(self, x):
        pass
		
    def degree(self):
        pass

    def der(self, d=1):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

class RealPolynomial(Polynomial):
    
    def find_root(self):
        pass

class QuadraticPolynomial(Polynomial):

    def solve(self):
        pass
    ```

- `test_polynomial.py`

    ```python
    # test_polynomial.py

    import pytest
    import random

    from polynomial import Polynomial, RealPolynomial, QuadraticPolynomial

    def test_init():
        poly_list = Polynomial([0, 1, 0, -2, 3, 0])
        assert str(poly_list) == '3x^4 - 2x^3 + x'
        assert repr(poly_list) == 'Polynomial [0, 1, 0, -2, 3]'

        poly_copy = Polynomial(poly_list)
        assert str(poly_copy) == '3x^4 - 2x^3 + x'
        assert repr(poly_copy) == 'Polynomial [0, 1, 0, -2, 3]'

        poly_dict = Polynomial({5: 3, 0: -1, 10: 7, 2: -4})
        assert str(poly_dict) == '7x^10 + 3x^5 - 4x^2 - 1'
        assert repr(poly_dict) == 'Polynomial [-1, 0, -4, 0, 0, 3, 0, 0, 0, 0, 7]'

        poly_args = Polynomial(1, 2, -3, 0, 5)
        assert str(poly_args) == '5x^4 - 3x^2 + 2x + 1'
        assert repr(poly_args) == 'Polynomial [1, 2, -3, 0, 5]'

        poly_const = Polynomial(10)
        assert str(poly_const) == '10'
        assert repr(poly_const) == 'Polynomial [10]'

    def test_eq():
        poly_zero = Polynomial([0] * 100)
        assert poly_zero == Polynomial(0)

        poly_zero_tail = Polynomial([1, 2, 0, -3, 0, 0, 0, 0, 0])
        assert poly_zero_tail == Polynomial([1, 2, 0, -3])

    def test_add():
        poly_lhs = Polynomial([2, 5, 0, 3, 2])
        poly_rhs = Polynomial(1, 3, 5, 0, 1, 0, 3)

        assert poly_lhs + poly_rhs == poly_rhs + poly_lhs
        assert str(poly_lhs + poly_rhs) == '3x^6 + 3x^4 + 3x^3 + 5x^2 + 8x + 3'
        assert str(14 + poly_lhs + 5) == '2x^4 + 3x^3 + 5x + 21'

        poly_lhs = Polynomial([2, 1, 2, 1])
        poly_rhs = Polynomial({3: 1, 1: 1, 0: 2, 2: 2})
        assert str(1 + poly_rhs + 2 + poly_lhs + 3) == '2x^3 + 4x^2 + 2x + 10'

        poly_lhs += poly_rhs
        assert str(poly_lhs) == '2x^3 + 4x^2 + 2x + 4'

    def test_der():
        poly = Polynomial([0, 4, 2, 2, 2, 1, 5])
        assert str(poly.der(0)) == str(poly)
        assert str(poly.der()) == '30x^5 + 5x^4 + 8x^3 + 6x^2 + 4x + 4'
        assert str(poly.der(5)) == '3600x + 120'

    def test_deg():
        poly_list = Polynomial([0, 1, 0, -2, 3, 0, 0])
        assert poly_list.degree() == 4

        poly_dict = Polynomial({5: 3, 0: -1, 10: 7, 2: -4})
        assert poly_dict.degree() == 10

        poly_const = Polynomial(10)
        assert poly_const.degree() == 0

    def test_sub():
        poly_lhs = Polynomial([1, 4, 1, 3])
        poly_rhs = Polynomial([4, 5, 5, 3])

        assert str(poly_lhs - poly_rhs) == '-4x^2 - x - 3'
        assert str(50 - poly_lhs - 4) == '-3x^3 - x^2 - 4x + 45'

    def test_call():
        poly = Polynomial([2, 1, 4, 1, 2, 5, 0])
        assert poly(0) == 2
        assert poly(1) == 15
        assert poly(2) == 220

    def test_mul():
        poly_lhs = Polynomial([9, 6, 1, 1, 9, 9, 8])
        poly_rhs = Polynomial([7, 5, 1, 0, 6])
        assert poly_lhs * poly_rhs == poly_rhs * poly_lhs
        assert str(
            poly_lhs * poly_rhs) == '48x^10 + 54x^9 + 62x^8 + 55x^7 + 116x^6 + 145x^5 + 123x^4 + 18x^3 + 46x^2 + 87x + 63'

    def test_iter():
        poly = Polynomial([1, 1, 5, 3, 9])
        pairs = [i for i in poly]
        true_pairs = [(0, 1), (1, 1), (2, 5), (3, 3), (4, 9)]
        for i in range(len(true_pairs)):
            assert pairs[i] == true_pairs[i]

    def test_real_poly():
        poly = RealPolynomial([2, 2, 9, 9, 7, 1, 8, 8])
        eps = 1e-6
        root = poly.find_root()
        assert abs(poly(root)) < eps

    def test_quadratic():
        poly = QuadraticPolynomial([-15, 7, 2])
        assert sorted(poly.solve()) == [-5.0, 1.5]
    ```
