#!/usr/bin/env python3

import argparse
from alg.brute_force import BruteForce
from env.cpp_env import CppEnvironment

class Tuner:
    def __init__(self, env, alg) -> None:
        self.env = env
        self.alg = alg

    def tune(self):
        while not self.alg.done():
            candidate = self.alg.next()
            result = self.env.step(candidate)
            self.alg.update(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--compile', type=str, help="File with compile command")
    parser.add_argument('--source', type=str, help="Source file")
    parser.add_argument('--env_def', type=str, help="Environment definition file")
    args = parser.parse_args()

    env = CppEnvironment(args)
    alg = BruteForce(args)
    t = Tuner(env, alg)
    t.tune()
