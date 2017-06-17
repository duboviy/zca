from zope.component import getUtility
from calc import IOperation, IScalaOperation
from zope.configuration import xmlconfig


def foldl(op, seq):
    op = IOperation(op)
    acc = seq[0]
    for n in seq[1:]:
        acc = op(acc, n)
    return acc


def main():
    # pip install zope.configuration
    xmlconfig.file('configure.zcml')

    assert foldl(getUtility(IOperation, '+'), range(11)) == 55
    assert foldl(getUtility(IScalaOperation, '/'), [64, 2, 2, 2, 2, 2]) == 2


if __name__ == '__main__':
    main()
