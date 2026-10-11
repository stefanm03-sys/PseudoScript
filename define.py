import pathlib
import os.path
class math:
    def entry(self, init):
        self.a = 0
        self.b = 0
        self.r = 0
    def add(self, init):
        self.r = int(self.a + self.b)
        return self.r

    def sub(self, init):
        self.r = int(self.a - self.b)
        return self.r
        
    def mul(self, init):
        self.r = int(self.a * self.b)
        return self.r
        
    def div(self, init):
        self.r = int(self.a / self.b)
        return self.r

    def remainder(self, init):
        self.r = int(self.a % self.b)
        return self.r

    def floordiv(self, init):
        self.r = int(self.a // self.b)
        return self.r
        
class operands:
    def entry(self, init):
        self.a = any
        self.b = any
        self.c = any
        self.r = any
    def regvar(self, init):
        self.b = "var"
        self.a = value
        self.r = name
        self.c = const
        vars.append(self.a.value)
        vars.append(self.r.name)
        return self.r
        
    def fixvar(self, init):
        self.b = "fvar"
        self.a = value
        self.r = name
        self.c = const
        vars.append(self.a.value)
        vars.append(self.r.name)
        vars.append(self.c.const)
        return self.r

    def ampersand(self, init):
        self.r = self.a, "&", self.b
        return self.r
    
    def log(self, init):
        self.r = "log({self.a})"
        if self.a == str:
            print(self.r)
        elif self.a == "true" or self.a == "false":
            print(self.r)
        else:
            print(float(self.r))
        return print(self.r)


def calculate(a, b, c):
    add = math.add
    sub = math.sub
    div = math.div
    mul = math.mul
    floordiv = math.floordiv
    remainder = math.remainder
    if math.add:
        return math.add
    elif math.sub:
        return math.sub
    elif math.div:
        return math.div
    elif math.mul:
        return math.mul
    elif math.remainder:
        return math.remainder
    elif math.floordiv:
        return math.floordiv
    else:
        return False
    
print("Starting..")
script = ".psc"
filename = "script"
testscript = "./script.psc"
with open(testscript, "r") as f:
    contents = f.read()

name = any
value = any
const = any
bool = "true" or "false"

vars = [
    {name, value, const}
]

print("ended")
