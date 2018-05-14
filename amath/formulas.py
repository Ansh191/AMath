from collections import OrderedDict as OD
from urllib.parse import urlencode
from urllib.request import urlopen

from amath.DataTypes.Function import Function
from amath.Errors import Failure


def formulaLookup(x):
    """Lookup formulas"""

    def wolfram_cloud_call(**args):
        arguments = dict([(key, arg) for key, arg in args.items()])
        try:
            result = urlopen("http://www.wolframcloud.com/objects/5c991864-3fbd-4b30-8200-d1a398aee0e2",
                             urlencode(arguments).encode("ascii"))
        except:
            raise Failure("Cannot connect to servers")
        return result.read()

    textresult = wolfram_cloud_call(x=x)
    return textresult.decode("ascii")


def formulaData(x):
    def wolfram_cloud_call(**args):
        arguments = dict([(key, arg) for key, arg in args.items()])
        try:
            result = urlopen("http://www.wolframcloud.com/objects/724d6409-5efb-4bcb-907a-6897aad95193",
                             urlencode(arguments).encode("ascii"))
        except:
            raise Failure("Cannot connect to servers")
        return result.read()

    textresult = wolfram_cloud_call(x=x)
    return textresult.decode("ascii")


Energy = Function(OD([('m', 'Real')]), 'm*(c**2)')

GravitationalForce = Function(OD([('m1', 'Real'), ('m2', 'Real'), ('d', 'Real')]), '(G*m1*m2)/(d**2)')

Pythagorean = Function(OD([('a', 'Real'), ('b', 'Real')]), 'sqrt((a**2)+(b**2))')

StandardNormalDistribution = Function(OD([('x', 'Real')]), '(e**(-(1/2.0)*(x**2)))/sqrt(2*pi)')

LorentzFactor = Function(OD([('v', "Real")]), "1.0/sqrt(1-(v**2)/(c**2))")

KineticEnergy = Function(OD([('m', "Real"), ('v', "Real")]), "(1/2.0)*m*(v**2)")

Momentum = Function(OD([('k', "Real"), ('m', "Real")]), "sqrt(2)*sqrt(k*m)")

MinimumPowerRequiredToMoveObject = Function(OD([('D', "Real"), ('m', "Real"), ('t', "Real")]), "(4*(D**2)*m)/(t**3)")

Velocity = Function(OD([('s', "Real"), ('t', "Real")]), "s/t")

Acceleration = Function(OD([('v', "Real"), ('t', "Real")]), 'v/t')


def HarmonicNumber(n):
    from .stats.stats import sum
    return sum(lambda x: 1 / x, 1, n)
