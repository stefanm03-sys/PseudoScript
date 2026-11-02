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
pscint = "number" # This is the integer type.
pscfloat = "decimal" # This is the floating point number type.
pscstr = "text" # This is the string type.
pscT = "true" # The string value for the boolean True.
pscF = "false" # The string value for the boolean False.
pscN = "nothing" # As before, this is the type for None.
name = any
value = any
const = any

class math: # This defines the class for mathematical operations.
    # init: One value used for mathematical numbers.
    # self: The other value used for math operations.
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
        if self.b or self.a == 0:
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
        return self.r
calculate = math()        
class operands: # Much like the previous class, this defines the operations instead of just math.
    # init: The value of the parameters.
    # self: The actual expression.
    def entry(self, init):
        self.a = init
        self.b = any
        self.c = any
        self.r = any
        # operands.entry.line = self.r
        
    def regvar(self, init):
        j = vars
        j = list()
        i = line
        i = line.split()

        self.r = init
        self.a = self
        const = False
        self.b = "variable"
        j.append([self.r, self.a, const])
        print(j)
        if name not in j:
            return NameError("Variable not found..")
        # var_expr = "{0} {1} {2}".format(self.b, name, init)
        return False
        
    def fixvar(self, init):
        vars = list()
        self.b = "constant"
        line = any
        j = line.split()
        name = j[1]
        init = j[2]
        const = True
        value = init
        print(j)
        if name not in vars:
            return NameError("Variable not found..")
        vars.append([name, value, const])
        # var_expr = "{0} {1} {2}".format(self.b, name, init)
        return False

    """ def reassign(self, init):
        self.b = any
        if self.b == "variable":
            operands.regvar(self, init)
        elif self.b == "constant":
            return ValueError("This is a constant..")

        pass; "This is assigned! Continue.." """
        
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
            return None
        
    def typenum(self, init):
        self.r = line
        if self.r.rstrip() == "decimal":
            return self.pscfloat
        elif self.r.rstrip() == "number":
            return self.pscint
        else:
            return None
        
    def typestr(self, init):
        self.r = line
        if self.r.rstrip() == "text":
            return self.pscstr
        else:
            return None

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
    # line = math.entry
    calculate.add(line)
    calculate.sub(line)
    calculate.mul(line)
    calculate.div(line)
    calculate.floordiv(line)
    calculate.remainder(line)

def oper(line):
    if "//" in line:
        str(line)
        return
    if line.startswith("log(") and line.endswith(")"):
        val = line[4:-1].strip().strip("\"'")
        print(val)
    if line.startswith("variable"):
        ops.regvar(line)
    if line.startswith("constant"):
        ops.fixvar(line)

def execIn():
    for line in contents:
        if line is math:
            calc(line)
        else:
            oper(line)
        print(line)

def execOut(any):
    print(any)
    pass

# print(output)
print()
print("[ Starting... ]")
# execIn()

line = "variable b 1" # Line reading test
ops.regvar(line) # Var test

print("^^^ In / Out ^^^")
print("vvv Stored Variables vvv")
print("{0}".format(vars))
print("[ Ended... ]")
"""
print("\n")
oper(line)
"""
