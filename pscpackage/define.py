import pathlib
import os.path
import inspect
# This is the building block of pseudoscript to define all of the code.

fext = ".psc"
fname = "script"
pack = "./pscpackage"
testscript = "./examplescript.psc"
standard = "./.psc"
output = any

# These are the strings for the types in psc.
pscint = "number"
pscfloat = "decimal"
pscstr = "text"
pscT = "true"
pscF = "false"
pscN = "nothing"
class math:
    def entry(self, init):
        self.a = self
        self.b = init
        self.r = int
        self.expr = str
        # math.entry.line = self.r
        
    def add(self, init):
        self.a = self
        self.b = init
        self.r = int(self.a + self.b)
        self.expr = "{0} + {1}".format(self.a, self.b)
        return self.r

    def sub(self, init):
        self.a = self
        self.b = init
        self.r = int(self.a - self.b)
        self.expr = "{0} - {1}".format(self.a, self.b)
        return self.r

    def mul(self, init):
        self.a = self
        self.b = init
        self.r = int(self.a * self.b)
        self.expr = "{0} * {1}".format(self.a, self.b)
        return self.r
        
    def div(self, init):
        self.a = self
        self.b = init
        self.r = int(self.a / self.b)
        if self.b == 0:
            return "There is a division by zero. Cannot run!"
        else:
            self.expr = "{0} / {1}".format(self.a, self.b)
            return self.r

    def remainder(self, init):
        self.a = self
        self.b = init
        self.r = int(self.a % self.b)
        self.expr = "{0} % {1}".format(self.a, self.b)
        return self.r

    def floordiv(self, init):
        self.a = self
        self.b = init
        self.r = int(self.a // self.b)
        self.expr = "{0} // {1}".format(self.a, self.b)
        return self.expr
calculate = math()        
class operands:
    def entry(self, init):
        self.a = init
        self.b = any
        self.c = any
        self.r = any
        # operands.entry.line = self.r
        
    def regvar(self, init):
        self.b = "var"
        self.a = init
        self.r = self
        self.line = self.b and self.a
        self.expr = "{0} {1} {2}".format(self.b, self.r, self.a)
        name = self.r
        value = self.a
        const = True
        vars  = []
        vars.append([name, value, const])
        return self.expr
        
    def fixvar(self, init):
        self.b = "var"
        self.a = init
        self.r = self
        self.line = self.b and self.a
        self.expr = "{0} {1} {2}".format(self.b, self.r, self.a)
        name = self.r
        value = self.a
        const = True
        vars  = []
        vars.append([name, value, const])
        return self.expr

    def ampersand(self, init):
        self.r = self
        self.a = init
        # self.line = self.r
        self.expr = "{0} & {1}".format(self.r, self.a)
        return self.expr
    
    def log(self, init):
        self.r = init
        self.a = self
        self.b = any
        self.expr = "log({0})".format(init)
        print(init)

    def comment(self, init):
        self.line = line
        self.r = init
        self.a = "//"
        if self.a and self.r:
            return print(str(self.a and self.r))
ops = operands()
class type:
    def entry(self, init):
        self.pscint = pscint
        self.pscstr = pscstr
        self.pscfloat = pscfloat
        self.pscT = pscT
        self.pscF = pscF
        self.pscN = pscN
        self.line = line
    
    def typebool(self, init):
        self.r = line
        if self.r.rstrip() == "true":
            return self.pscT
        elif self.r.rstrip() == "false":
            return self.pscF
        else:
            return False
        
    def typenum(self, init):
        self.r = line
        if self.r.rstrip() == "decimal":
            return self.pscfloat
        elif self.r.rstrip() == "number":
            return self.pscint
        else:
            return False
        
    def typestr(self, init):
        self.r = line
        if self.r.rstrip() == "text":
            return self.pscstr

    def typenone(self, init):
        self.r = line
        if self.r.rstrip() == "nothing":
            return self.pscN
types = type()



with open(testscript, "r") as f:
    contents = f.read()
    contents = contents.splitlines()
    line = f.readline()

def calc(line):
    line = math.entry
    for line in contents:
        calculate.add(line)
        calculate.sub(line)
        calculate.mul(line)
        calculate.div(line)
        calculate.floordiv(line)
        calculate.remainder(line)

def oper(line):
    line = operands.entry
    for line in contents:
        # ops.ampersand(line)
        if "//" in line:
            str(line)
            continue
        elif line.startswith("log(") and line.endswith(")"):
            val = line[4:-1].strip().strip("\"'")
            execOut(val)
        elif line.startswith("var"):
            ops.regvar(line)
        elif line.startswith("constant"):
            ops.fixvar(line)

def execIn():
    print("[ Starting... ]")
    for line in contents:
        # print(line)
        if line is math:
            calc(line)
            break
        else:
            oper(line)
            break

def execOut(any):
    print(any)
    print("^^^ Output ^^^")
    pass
print(output)
name = any
value = any
const = any
vars = [
    {"variable": name, "stored-value": value, "fixed": const}
]
execIn()
print("vvv Stored Variables vvv")
print("{0}".format(vars))
print("[ ended... ]")
"""
print("\n")
oper(line)
"""
