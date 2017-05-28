from zope.component import getGlobalSiteManager

from IOperation import IOperation
from utils import Plus, Minus


gsm = getGlobalSiteManager()

gsm.registerUtility(Plus(), IOperation, '+')
gsm.registerUtility(Minus(), IOperation, '-')
