from zope.interface import Interface


class IOperation(Interface):
    def __call__(a, b):
        """Performs operation on two operands"""


class ISpecialOperation(Interface):
    """Special operation"""
