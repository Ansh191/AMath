import time
import _random


class Random(_random.Random):
    def __init__(self, seed = int(time.time())):
        self.seed = seed
        self._seed = seed

    def reset(self):
        self._seed = self.seed

    def rndint(self, s = 0, l = 10):
        if s >= l:
            raise ValueError("s is greater than or equal to l")
        num = pow(self._seed, 2) + 1234
        strnum = str(num)
        strnum += "37"
        mid = int(strnum[1:len(strnum) - 1])
        self._seed = int(mid ** (1 / 11))
        return mid
