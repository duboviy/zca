from zope.component import getUtility
from IOperation import IOperation
from zope.interface.interfaces import ComponentLookupError

import registrator


def calc(expr):
    a, op, b = expr.split()
    return getUtility(IOperation, op)(eval(a), eval(b))


assert calc('2 + 2') == 4
assert calc('2 - 2') == 0
assert calc('2 - 0.2') == 1.8

try:
    assert calc('2 * 2') == 4
except:
    pass
else:
    raise RuntimeError("Should raise ComponentLookupError because there is no operation * utility")
