# Чтобы все корректно работало, не меняйте названия файлов 
# или если вы их просто копируете, то создавайте у себя 
# файлы с названиями указанными ниже.

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