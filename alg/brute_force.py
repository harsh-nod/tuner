from alg.algorithm import Algorithm
import itertools
from functools import reduce
import json

class BruteForce(Algorithm):
    def __init__(self, args) -> None:
        with open(args.env_def, 'r') as f:
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
        self.candidate = next(self.candidates)
        return {x:y for x, y in zip(self.variables, candidate)}

    def update(self, result):
        with open('history.json', 'r+') as f:
            data = json.load(f)
            data["history"].append(
                {"candidate": self.candidate, "objective": result}
            )
            f.seek(0)
            json.dump(data, f, indent=4)

    def done(self):
        return self.count == self.num_candidates - 1

