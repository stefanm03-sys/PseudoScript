import pathlib
import os.path
# This is the building block of pseudoscript to define all of the code.

fext = ".psc"
fname = "script"
pack = "./pscpackage"
testscript = "./examplescript.psc"
standard = "./.psc"
line = " "

# These are the strings for the types in psc.
pscint = "number"
pscfloat = "decimal"
pscstr = "text"
pscT = "true"
pscF = "false"
pscN = "nothing"

with open(testscript, "r") as f:
    contents = f.read()
    contents = contents.splitlines()
    line = f.readline()
class math:
    def entry(self, init):
        self.a = 0
        self.b = 0
        self.r = 0
        self.expr = " "
        math.entry.line = self.r
        
    def add(self, init):
        self.line = self.r
        self.r = int(self.a + self.b)
        self.expr = "{0} + {1}".format(self.a, self.b)
        return self.expr

    def sub(self, init):
        self.line = self.r
        self.r = int(self.a - self.b)
        self.expr = "{0} - {1}".format(self.a, self.b)
        return self.expr
        
    def mul(self, init):
        self.line = self.r
        self.r = int(self.a * self.b)
        self.expr = "{0} * {1}".format(self.a, self.b)
        return self.expr
        
    def div(self, init):
        self.line = self.r
        self.r = int(self.a / self.b)
        self.expr = "{0} / {1}".format(self.a, self.b)
        return self.expr

    def remainder(self, init):
        self.line = self.r
        self.r = int(self.a % self.b)
        self.expr = "{0} % {1}".format(self.a, self.b)
        return self.expr

    def floordiv(self, init):
        self.line = self.r
        self.r = int(self.a // self.b)
        self.expr = "{0} // {1}".format(self.a, self.b)
        return self.expr
        
class operands:
    def entry(self, init):
        self.a = any
        self.b = any
        self.c = any
        self.r = any
        operands.entry.line = self.r
        
    def regvar(self, init):
        self.b = "var"
        self.a = value
        self.r = name
        self.c = const
        self.line = self.b and self.a
        self.expr = "{0} {1}".format(self.r, self.a)
        vars.append(self.a.value)
        vars.append(self.r.name)
        return self.expr
        
    def fixvar(self, init):
        self.b = "fvar"
        self.a = value
        self.r = name
        self.c = const
        self.line = self.b and self.a
        self.expr = "{0} {1}".format(self.r, self.a)
        vars.append(self.a.value)
        vars.append(self.r.name)
        vars.append(self.c.const)
        return self.expr

    def ampersand(self, init):
        self.r = self.a, "&", self.b
        self.line = self.r
        self.expr = "{0} {1}".format(self.r, self.a)
        return self.expr
    
    def log(self, init):
        self.a = any
        self.r = line
        self.expr = "log(\"{0}\")".format(self.a)
        if self.a == str:
            print(self.r)
        elif self.a == "true" or self.a == "false":
            print(self.r)
        else:
            print(float(self.r))
        return self.expr

    def comment(self, init):
        self.line = line
        self.r = " "
        self.a = "//"
        if self.a and self.r:
            return print(str(self.a and self.r))

class type:
    def entry(self, init):
        self.pscint = pscint
        self.pscstr = pscstr
        self.pscfloat = pscfloat
        self.pscT = pscT
        self.pscF = pscF
        self.pscN = pscN
    
    def typebool(self, init):
        if self.pscT in line:
            return True
        elif self.pscF in line:
            return False
        elif self.pscN in line:
            return None
        else:
            return 0
            
    def typenum(self, init):
        if self.pscint in line:
            return int()
        elif self.pscfloat in line:
            return float()
        else:
            return 0
            
    def typestr(self, init):
        if self.pscstr in line:
            return str()
        else:
            return 0

""""""

def calc(line):
    add = math.add
    sub = math.sub
    div = math.div
    mul = math.mul
    floordiv = math.floordiv
    remainder = math.remainder
    line = math.entry
    for line in contents:
        if line == math.add:
            return math.add
        elif line == math.sub:
            return math.sub
        elif line == math.div:
            return math.div
        elif line == math.mul:
            return math.mul
        elif line == math.remainder:
            return math.remainder
        elif line == math.floordiv:
            return math.floordiv
        else:
            return False

def operate(line):
    regvar = operands.regvar
    fixvar = operands.fixvar
    ampersand = operands.ampersand
    log = operands.log
    line = operands.entry
    for line in contents:
        if line == operands.regvar:
            return operands.regvar
        elif line == operands.fixvar:
            return operands.fixvar
        elif line == operands.ampersand:
            return operands.ampersand
        elif line == operands.log:
            return operands.log
        else:
            return False

def execute():
    print("Starting..")
    with open(testscript, "r") as f:
        for line in contents:
            print(line)
            operate(line)
            # calc(line)

name = any
value = any
const = any
vars = [
    {name, value, const}
]