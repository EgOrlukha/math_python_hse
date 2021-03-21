Домашнее задание состоит из двух частей. 

- Реализация класса многочленов, сдается в **[Контест](https://contest.yandex.ru/contest/23118). 
Дедлайн:** 13.12 23:59
- Задания `CLI, Github, GCD и Testing` сдаются в **Anytask**. 
**Дедлайн**: 20.12 23:59.

## [5 + 4 баллов] Класс многочленов

В этой задаче вам нужно реализовать класс `Polynomial` для работы с многочленами. Методы, которые будут проверяться в задаче уже определены в файле `polynomial.py`. Вам не запрещается добавлять свои функции, переменные или методы, однако запрещается менять названия предоставленных методов. Разрешается использовать только стандартную библиотеку Python. 

**Совет #1:** заранее подумайте, какую структуру данных использовать для хранения коэффициентов.

**Совет #2:** продумайте реализацию метода `__str__`, при грамотном подходе код метода должен занимать не более 30 строчек.

За прохождение открытых тестов (есть файл ниже) ставится 5 баллов.
За прохождение приватных тестов ставится еще 4 балла.

### Требования к реализации

- Конструктор `__init__` позволяет построить многочлен
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

        Как видно из примера, args - это кортеж из всех переданных аргументов функции, и с переменной можно работать также, как и с кортежем

- Перегруженный метод `__repr__`, который будет возвращать строку вида: `Polynomial <список коэффициентов>`

    ```python
    In[10] : Polynomial(1, 2, 3, 0, 0, 0, 5, 0, 0)
    Out[10]: Polynomial [1, 2, 3, 0, 0, 0, 5]

    In[11] : repr(Polynomial(2, 3))
    Out[11]: Polynomial [2, 3]
    ```

    **Примечание:**

    - [Difference between str and repr?](https://stackoverflow.com/questions/1436703/difference-between-str-and-repr)
- Перегруженный метод `__str__`, возвращающий строковое представление объекта. Многочлен должен выводиться начиная от старшей степени. Должны быть приведены подобные, отсутствовать нулевые коэффициенты, а также не должно быть единичных коэффициентов и степеней. Примеры:

    ```python
    In[7] : print(Polynomial(0, 2, 0, 5))
    Out[7]: 5x^3 + 2x

    In[8] : print(Polynomial([7, -2, 0, 1]))
    Out[8]: x^3 - 2x + 7

    In[9] : print(Polynomial([7, -2, 0, -1]))
    Out[9]: -x^3 - 2x + 7
    ```

- Перегруженные операторы `+, - (в том числе унарный)`. Также должны поддерживаться арифметические операции с числами.
- Перегруженный оператор `==` для сравнение многочленов на равенство между собой и с числами
- Метод `degree` возвращающий степень многочлена

    ```python
    In[13] : poly = Polynomial(1, 2, 3)
        ...: print(poly.degree())
    Out[13]: 2
    ```

- Метод `der(self, d=1)` который вычисляет производную степени `d`
- Перегруженный оператор `__call__` позволяющий вычислить значение многочлена в точке

    ```python
    In[12] : poly = Polynomial(1, 2, 3)
        ...: print(poly(1))
    Out[12]: 6
    ```

- Перегруженный оператор `*`, в том числе и для умножения на числа.
- Перегруженные методы `__iter__` и `__next__` позволяющие проитерироваться по многочлену. На каждом шаге итерации должна возвращаться пара вида `(степень, коэффициент)`

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
- Производный класс `RealPolynomial`
    - Данный класс является многочленом нечетной степени от вещественных коэффициентов
    - Создайте ошибку `NotOddDegreeException` и бросайте ее в случае, когда пытаются создать полином `RealPolynomial` четной степени
    - Необходимо реализовать метод `find_root`, возвращающий корень многочлена с точностью заданной точностью `eps`.
- Производный класс `QuadraticPolynomial`
    - Данный класс является многочленом степени не выше 2
    - Создайте ошибку `DegreeIsTooBigException` и бросайте ее в случае, когда пытаются создать полином `QuadraticPolynomial` степени больше 2
    - Необходимо реализовать метод `solve`, возвращающий список содержащий действительные корни многочлена (соответственно, размер списка равен либо 0, либо 1, либо 2)

### Тестирование

- Файл, содержащий реализацию должен называться `polynomial.py`
- Положите файл с тестами (`test_polynomial.py`) в ту же папку, где лежит `polynomial.py`.
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

        def __repr__(self):

        def __str__(self):

        def __eq__(self, other):

        def __add__(self, other):

        def __radd__(self, other):

        def __neg__(self):

        def __sub__(self, other):

        def __rsub__(self, other):

        def __call__(self, x):
    		
        def degree(self):

        def der(self, d=1):

        def __mul__(self, other):

        def __rmul__(self, other):

        def __iter__(self):

        def __next__(self):

    class RealPolynomial(Polynomial):
        def find_root(self):
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

## [1 балл] [CLI](https://ru.wikipedia.org/wiki/Интерфейс_командной_строки)

С помощью `argparse` добавьте интерфейс командной строки для запуска различных операций с многочленами. В задании необходимо реализовать следующие команды:

1. Умножение двух многочленов
    - `lhs` - коэффициенты первого многочлена, `rhs` - второго

    ```python
    $ python3 main.py multiply --lhs 1 2 3 -- rhs 4 1
    ```

2. Нахождение производной
    - `degree` - степень производной

    ```python
    $ python3 main.py derrivative 1 5 3 4 2 --degree 3
    ```

3. Решение квадратного уравнения

    ```python
    $ python3 main.py solve-quadratic 4 2 4
    ```

4. Поиск корня многочлена нечетной степени
    - `eps` - точность, с которой необходимо найти корень

    ```python
    $ python3 main.py find-root 1 5 3 2 5 7 --eps 1e-7
    ```

Для каждой команды необходимо краткое описание с помощью аргумента `help`.

Логику связанную с применением `argparse` предлагается вынести в отдельный файл `main.py`. Также, можете реализовать ее внутри polynomial.py, только в таком случае необходимо выполнять парсинг аргументов внутри условия `if __name__ == "__main__"`:

- [What does `if __name__ == "__main__"` do?](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)

## [1 балл] Github

В данной части необходимо разобраться с [github](https://github.com/) и разместить свое решение на этой платформе. Также, оформите небольшой `README`, в котором будет краткое описание проделанной работы.

- [Hello world](https://guides.github.com/activities/hello-world/) (не обязательно создавать ветку и делать `pull request`, достаточно просто сделать `push` в `master`)
- [Github Tutorial For Beginners - Github Basics for Mac or Windows & Source Control Basics](https://www.youtube.com/watch?v=0fKg7e37bQE)
- [How to Write Beautiful and Meaningful README](https://blog.bitsrc.io/how-to-write-beautiful-and-meaningful-readme-md-for-your-next-project-897045e3f991)
- [Basic writing and formatting syntax](https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax)
- [Markdown Cheetsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## [1 балл] GCD

Добавьте следующую функциональность в класс многочленов:

- Перегруженный оператор `%`, в том числе и для взятия остатка при делении на числа.
- Перегруженный оператор `/`, в том числе и для деления на числа, который возвращает пару `(q, r)` - частное и остаток.
- Метод `gcd` позволяющий вычислить НОД двух многочленов.

## [1 балл] Testing

- Добавьте тесты на методы из предыдущего задания с помощью фрэймворка `pytest`.
- С помощью утилиты [coverage](https://coverage.readthedocs.io/en/coverage-5.3/) добейтесь 100% покрытия для реализованных в этом задании методов.
