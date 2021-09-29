## Что такое "красивый код" и зачем это надо?

В домашних заданиях в контесте ваш код дополнительно проверяется на его "красоту-чистоту" - стайлкод по стандарту PEP8. 
В целом это такое общее правило, как, например, то, что перед запятой при написании текста пробел не ставится, а после ставится ровно один, или то, 
что предложение должно начинаться с заглавной буквы и заканчиваться знаком препинания, или то, что абзац должен начинаться с отступа. 
В программировании такая же логика - **код должен быть читаемым**. 

1. [Дзен Питона](https://tyapk.ru/blog/post/the-zen-of-python)
2. [Руководство по PEP8 на русском языке](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html)

При сдаче заданий в Я.Контест, если ваш код не подходит под стандарт, то вы будете видеть ошибку `PCF`, а в отчете посылки увидите вывод вот такого вида сообщений:

```bash
file.py:line 33 symbol:1: E302 expected 2 blank lines, found 1
def create_deadlines(weekstart, mode):
^
    Separate top-level function and class definitions with two blank
    lines.

    Method definitions inside a class are separated by a single blank
    line.

    Extra blank lines may be used (sparingly) to separate groups of
    related functions.  Blank lines may be omitted between a bunch of
    related one-liners (e.g. a set of dummy implementations).

    Use blank lines in functions, sparingly, to indicate logical
    sections.

    Okay: def a():\n    pass\n\n\ndef b():\n    pass
    Okay: def a():\n    pass\n\n\nasync def b():\n    pass
    Okay: def a():\n    pass\n\n\n# Foo\n# Bar\n\ndef b():\n    pass
    Okay: default = 1\nfoo = 1
    Okay: classify = 1\nfoo = 1

    E301: class Foo:\n    b = 0\n    def bar():\n        pass
    E302: def a():\n    pass\n\ndef b(n):\n    pass
    E302: def a():\n    pass\n\nasync def b(n):\n    pass
    E303: def a():\n    pass\n\n\n\ndef b(n):\n    pass
    E303: def a():\n\n\n\n    pass
    E304: @decorator\n\ndef a():\n    pass
    E305: def a():\n    pass\na()
    E306: def a():\n    def b():\n        pass\n    def c():\n        pass
    
file.py:line 92 symbol:50: E225 missing whitespace around operator
        penalty = int((late / day_sec)) + (late /day_sec) % 1 // 0.5
                                                 ^
                                                                                              ^
    Surround operators with a single space on either side.

    - Always surround these binary operators with a single space on
      either side: assignment (=), augmented assignment (+=, -= etc.),
      comparisons (==, <, >, !=, <=, >=, in, not in, is, is not),
      Booleans (and, or, not).

    - If operators with different priorities are used, consider adding
      whitespace around the operators with the lowest priorities.

    Okay: i = i + 1
    Okay: submitted += 1
    Okay: x = x * 2 - 1
    Okay: hypot2 = x * x + y * y
    Okay: c = (a + b) * (a - b)
    Okay: foo(bar, key='word', *args, **kwargs)
    Okay: alpha[:-i]

    E225: i=i+1
    E225: submitted +=1
    E225: x = x /2 - 1
    E225: z = x **y
    E225: z = 1and 1
    E226: c = (a+b) * (a-b)
    E226: hypot2 = x*x + y*y
    E227: c = a|b
    E228: msg = fmt%(errno, errmsg)

file.py:line 140 symbol:20: E231 missing whitespace after ','
    dataframe.loc[:,'fio':].to_csv(filename + '.csv', index=False)
                   ^
    Each comma, semicolon or colon should be followed by whitespace.
    
    Okay: [a, b]
    Okay: (3,)
    Okay: a[1:4]
    Okay: a[:4]
    Okay: a[1:]
    Okay: a[1:4:2]
    E231: ['a','b']
    E231: foo(bar,baz)
    E231: [{'a':'b'}]
```

Соответственно, в примере вывода сообщения говорится, что в сданном коде есть как минимум три вида несоответствия стандарту PEP8. 
Показывается только первая ошибка и ее описание внутри одного типа ошибки. 
Например, если вы в двух местах кода забыли поставить нужный пробел, то вывод сообщения покажет только первый из них, а второй вы должны найти либо сами, 
либо заново сдав код с уже исправленной первой ошибкой. 

На codereview ассистенты также вправе снизить оценку за несоответствие данным требованиям. 
