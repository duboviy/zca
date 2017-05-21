from zope.interface import invariant, Interface, implements

from utils import Plus


def binary_float_operation(obj):
    res = obj(2, 2.1)
    assert isinstance(res, float), 'Operation should return float'


class IOperation(Interface):
    def __call__(a, b):
        """Performs operation on two operands"""

    invariant(binary_float_operation)


class IntPlus(object):
    implements(IOperation)

    def __call__(self, a, b):
        return int(a + b)


IOperation.validateInvariants(Plus())
try:
    IOperation.validateInvariants(IntPlus())
except AssertionError:
    pass
else:
    raise RuntimeError("Should raise AssertionError because IOperation implementation should return float")
