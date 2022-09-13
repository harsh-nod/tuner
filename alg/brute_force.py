from algorithm import Algorithm
import itertools
from functools import reduce
import json

class BruteForce(Algorithm):
    def __init__(self, args) -> None:
        with open(args.source, 'r') as f:
            data = json.load(f)
        self.variables = []
        self.ranges = []
        for k, v in data.items():
            self.variables.append(k)
            self.ranges.append(v)
        self.num_candidates = reduce(lambda x, y : x * y, [len(x) for x in self.ranges])
        self.candidates = itertools.product(self.ranges)
        self.count = 0

    def next(self):
        self.count += 1
        candidate = next(self.candidates)
        return {x:y for x, y in zip(self.variables, candidate)}

    def done(self):
        return self.count == self.num_candidates - 1

