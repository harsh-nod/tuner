from env.environment import Environment
import json
import subprocess

class CppEnvironment(Environment):
    def __init__(self, args) -> None:
        with open(args.compile, 'r') as f:
            data = json.load(f)
        self.compile_cmd = [data["compiler"]] + data["compiler_flags"]
        self.exec_cmd = [data["executable"]] + data["executable_flags"]
        self.source = args.source
        with open(args.env_def, 'r') as f:
            data = json.load(f)
        self.variables = [k for k in data.keys()]

    def update_source(self, x):
        with open(self.source, 'r') as f:
            data = f.read()
        for k, v in x.items():
            data = data.replace('$' + k, str(v))
        self.candidate_file = self.source[:-5]
        with open(self.candidate_file, 'w') as f:
            f.write(data)

    def parse(self, output):
        return output

    def step(self, x):
        self.update_source(x)
        print(' '.join(self.compile_cmd))
        p = subprocess.Popen(self.compile_cmd, stdout=subprocess.PIPE)
        p.wait()
        print(' '.join(self.exec_cmd))
        p = subprocess.Popen(self.exec_cmd, stdout=subprocess.PIPE)
        output = p.communicate()
        p.wait()
        metrics = self.parse(output)
        return metrics
