import random


def get_digit():
    return random.randint(1, 9)


from zope.component.factory import Factory
factory = Factory(get_digit, 'random_digit', 'Gives a random digit')


from zope.component import getGlobalSiteManager
from zope.component.interfaces import IFactory

gsm = getGlobalSiteManager()
gsm.registerUtility(factory, IFactory, 'random_digit')

from zope.component import getUtility
assert 1 <= getUtility(IFactory, 'random_digit')() <= 9     # creates digit

from zope.component import createObject
assert 1 <= createObject('random_digit') <= 9   # also creates a digit
