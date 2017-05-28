from zope.interface import implements

from IOperation import IOperation


class Plus(object):
    implements(IOperation)

    def __call__(self, a, b):
        return a + b


class Minus(object):
    implements(IOperation)

    def __call__(self, a, b):
        return a - b


### alternative way to make utility component (using not class-adviser on class level -> using function classImplements)
# from zope.interface import classImplements
# classImplements(Host, IHost)
### also in Python 2.6 and later you can use class decorator @implementer(IFoo)
