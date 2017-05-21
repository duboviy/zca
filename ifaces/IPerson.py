from zope.interface import Attribute


class IPerson(Interface):
    name = Attribute('Name of the person')
