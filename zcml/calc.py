from zope.interface import Interface, implements
from zope.component import getUtility


class IOperation(Interface):
    def __call__(a, b):
        """Performs operation on two operands"""


class Plus(object):
    implements(IOperation)

    def __call__(self, a, b):
        return a + b


# plus = Plus() # not needed if you use factory instead of component in configure.zcml


class Minus(object):
    implements(IOperation)

    def __call__(self, a, b):
        return a - b


# minus = Minus() # not needed if you use factory instead of component in configure.zcml


def eval(expr):
    a, op, b = expr.split()
    return getUtility(IOperation, op)(float(a), float(b))
