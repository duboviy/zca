from zope.configuration import xmlconfig
from zope.component import getUtility

from calc import eval


def main():
    # pip install zope.configuration
    xmlconfig.file('configure.zcml')

    assert eval('2 + 2') == 4
    assert eval('2 - 2') == 0


if __name__ == '__main__':
    main()
