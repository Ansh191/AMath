from urllib.parse import urlencode
from urllib.request import urlopen

from amath.DataTypes.Function2 import Function
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

    import re
    textresult = wolfram_cloud_call(x=x)  # .decode("ascii")
    # print(textresult)
    textresult = textresult.split(b"==")[1]
    var = re.findall(b"(\w+)(?=\",)", textresult)
    # print(var)
    textresult = textresult.replace(b"QuantityVariable[\"", b"")
    textresult = re.sub(b'", "\w+"]', b"", textresult).replace(b"^", b"**")
    # print(textresult)
    return Function(textresult.decode(), list(map(bytes.decode, var)))


EnergyRelativistic = Function('m*(c**2)', {'m': 'Real'})

GravitationalForce = Function('(G*m1*m2)/(d**2)', {'m1': 'Real', 'm2': 'Real', 'd': 'Real'})

Pythagorean = Function('sqrt((a**2)+(b**2))', {'a': 'Real', 'b': 'Real'})

StandardNormalDistribution = Function('(e**(-(1/2.0)*(x**2)))/sqrt(2*pi)', {'x': 'Real'})

NormalDistribution = Function('1/(e**((-m + x)**2/(2.*s**2))*sqrt(2*pi)*s)', {'m': 'Real', 's': 'Real', 'x': 'Real'})

LorentzFactor = Function("1.0/sqrt(1-(v**2)/(c**2))", {'v': 'Real'})

KineticEnergy = Function("(1/2.0)*m*(v**2)", {'m': 'Real', 'v': 'Real'})

Momentum = Function("m * v", {'m': 'Real', 'v': 'Real'})

MinimumPowerRequiredToMoveObject = Function('(4*(D**2)*m)/(t**3)', {'D': 'Real', "m": 'Real', 't': 'Real'})

Velocity = Function("s/t", {'s': 'Real', 't': 'Real'})

Acceleration = Function('dv/dt', {'dv': 'Real', 'dt': 'Real'})

EscapeVelocity = Function("sqrt(2)*sqrt((G * m)/r)", {"m": "real", "r": "real"})

GravitationalPotentialEnergy = Function("g * h * m", {"g": "real", "h": "real", "m": 'real'})

Density = Function("M / V", {"M": 'real', "V": "real"})

NewtonsSecondLawConstantMass = Function("a * m", {"a": 'real', 'm': 'real'})

MomentumKineticEnergy = Function("sqrt(2)*sqrt(k*m)", {'k': 'Real', 'm': 'Real'})

Work = Function("a * d * m", {"a": "real", "d": 'real', "m": 'real'})

TimeDilationRelativistic = Function("t/sqrt(1 - v**2/c**2)", {"t": 'Real', "v": 'Real'})

TimeDilationGravitational = Function("t/sqrt(1 - (g*r)/c**2)", {"t": 'real', "g": 'real', "r": 'real'})


def HarmonicNumber(n):
    from .stats.stats import sum
    return sum(lambda x: 1 / x, 1, n)
