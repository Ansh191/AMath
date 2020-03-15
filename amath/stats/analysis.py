from ..constants import inf


def absmin(x):
    m = inf
    for i in x:
        if abs(i) < m:
            m = i

    return m


def absmax(x):
    m = 0
    for i in x:
        if abs(i) > m:
            m = i

    return m


def variance(samples):
    var = 0
    t = samples[0]
    for i in range(1, len(samples)):
        t += samples[i]
        diff = ((i + 1) * samples[i]) - t
        var += (diff * diff) / ((i + 1.0) * i)

    return var / (len(samples) - 1)


def popvariance(samples):
    var = 0
    t = samples[0]
    for i in range(1, len(samples)):
        t += samples[i]
        diff = ((i + 1) * samples[i]) - t
        var += (diff * diff) / ((i + 1.0) * i)

    return var / (len(samples))


def standarddeviation(samples):
    return variance(samples) ** .5


def popstandarddeviation(samples):
    return popvariance(samples) ** .5
