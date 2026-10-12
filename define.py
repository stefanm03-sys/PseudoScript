import pathlib
import os.path
extension = ".psc"
filename = "script"
testscript = "./script.psc"
line = " "
num = "num"
deci = "deci"
text = "text"
true = "true"
false = "false"
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
        self.line = self.r
        self.r = ""
        self.a = "//"
        if self.a and self.r:
            print(str(self.a and self.r))

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
        if line == math.add.expr:
            return math.add
        elif line == math.sub.expr:
            return math.sub
        elif line == math.div.expr:
            return math.div
        elif line == math.mul.expr:
            return math.mul
        elif line == math.remainder.expr:
            return math.remainder
        elif line == math.floordiv.expr:
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
        if line == operands.regvar.expr:
            return operands.regvar
        elif line == operands.fixvar.expr:
            return operands.fixvar
        elif line == operands.ampersand.expr:
            return operands.ampersand
        elif line == operands.log.expr:
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

execute()
name = any
value = any
const = any
vars = [
    {name, value, const}
]
print("{0}".format(vars))
print("ended")
