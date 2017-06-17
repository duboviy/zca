from zope.interface import Interface, implements
from zope.component import getUtility
from zope.component import adapts


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



class IScalaOperation(Interface):
    def apply(a, b):
        ''' performs operation on two operands '''


class Division(object):
    implements(IScalaOperation)

    def apply(self, x, y):
        return x / y


class ScalaOperationAdapter(object):
    implements(IOperation)
    adapts(IScalaOperation)

    def __init__(self, scala_op):
        self.scala_op = scala_op

    def __call__(self, a, b):
        return self.scala_op.apply(a, b)
