from zope.interface.verify import verifyObject, verifyClass
from zope.interface.exceptions import DoesNotImplement

from IOperation import IOperation
from utils import Plus


assert verifyClass(IOperation, Plus) == True
assert verifyObject(IOperation, Plus()) == True

try:
    verifyObject(IOperation, object())
except DoesNotImplement:
    pass
else:
    raise RuntimeError("Should raise DoesNotImplement because there is no implementation")
