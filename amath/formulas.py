from amath.DataTypes.Function import Function
from amath.Errors import Failure


def formulaLookup(x):
    """Lookup formulas"""
    from urllib import urlencode
    from urllib2 import urlopen

    def wolfram_cloud_call(**args):
        arguments = dict([(key, arg) for key, arg in args.iteritems()])
        try:
            result = urlopen("http://www.wolframcloud.com/objects/5c991864-3fbd-4b30-8200-d1a398aee0e2",
                             urlencode(arguments))
        except:
            raise Failure("Cannot connect to servers")
        return result.read()

    textresult = wolfram_cloud_call(x=x)
    return textresult


def formulaData(x):
    from urllib import urlencode
    from urllib2 import urlopen

    def wolfram_cloud_call(**args):
        arguments = dict([(key, arg) for key, arg in args.iteritems()])
        try:
            result = urlopen("http://www.wolframcloud.com/objects/724d6409-5efb-4bcb-907a-6897aad95193",
                             urlencode(arguments))
        except:
            raise Failure("Cannot connect to servers")
        return result.read()

    textresult = wolfram_cloud_call(x=x)
    return textresult


Energy = Function(dict(m='Real'), 'm*(c**2)')

GravitationalForce = Function(dict(m1='Real', m2='Real', d='Real'), '(G*m1*m2)/(d**2)')

Pythagorean = Function(dict(a='Real', b='Real'), 'sqrt((a**2)+(b**2))')

StandardNormalDistribution = Function(dict(x='Real'), '(e**(-(1/2.0)*(x**2)))/sqrt(2*pi)')

LorentzFactor = Function(dict(v="Real"), "1.0/sqrt(1-(v**2)/(c**2))")

KineticEnergy = Function(dict(m="Real", v="Real"), "(1/2.0)*m*(v**2)")

Momentum = Function(dict(k="Real", m="Real"), "sqrt(2)*sqrt(k*m)")

MinimumPowerRequiredToMoveObject = Function(dict(D="Real", m="Real", t="Real"), "(4*(D**2)*m)/(t**3)")
