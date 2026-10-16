import pathlib
import os.path
import inspect
# This is the building block of pseudoscript to define all of the code.

fext = ".psc"
fname = "script"
pack = "./pscpackage"
testscript = "./examplescript.psc"
standard = "./.psc"

# These are the strings for the types in psc.
pscint = "number"
pscfloat = "decimal"
pscstr = "text"
pscT = "true"
pscF = "false"
pscN = "nothing"

name = any
value = any
const = any
vars = {
    "{0}".format(name): (value, const),

}
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
        self.a = 0
        self.b = 0
        self.c = line
        self.r = int(self.a + self.b)
        self.expr = "{0} + {1}".format(self.a, self.b)
        if self.c.rstrip() == self.expr:
            return self.r

    def sub(self, init):
        self.a = 0
        self.b = 0
        self.c = line
        self.r = int(self.a - self.b)
        self.expr = "{0} - {1}".format(self.a, self.b)
        if self.c.rstrip() == self.expr:
            return self.r

    def mul(self, init):
        self.a = 0
        self.b = 0
        self.c = line
        self.r = int(self.a * self.b)
        self.expr = "{0} * {1}".format(self.a, self.b)
        if self.c.rstrip() == self.expr:
            return self.r
        
    def div(self, init):
        self.a = 1
        self.b = 1
        self.c = line
        self.r = int(self.a / self.b)
        if self.b == 0:
            return "There is a division by zero. Cannot run!"
        self.expr = "{0} / {1}".format(self.a, self.b)
        if self.c.rstrip() == self.expr:
            return self.r

    def remainder(self, init):
        self.a = 1
        self.b = 1
        self.c = line
        self.r = int(self.a % self.b)
        self.expr = "{0} % {1}".format(self.a, self.b)
        if self.c.rstrip() == self.expr:
            return self.r

    def floordiv(self, init):
        self.a = 1
        self.b = 1
        self.c = line
        self.r = int(self.a // self.b)
        self.expr = "{0} // {1}".format(self.a, self.b)
        if self.c.rstrip() == self.expr:
            return self.r
        
class operands:
    def entry(self, init):
        self.a = any
        self.b = any
        self.c = any
        self.r = any
        operands.entry.line = self.r
    
    def parentheses(self, init):
        self.a = "("
        self.r = any
        self.b = ")"
        self.expr = "{0} {1} {2}".format(self.a, self.r, self.b)
        return True
        
    def regvar(self, init):
        self.b = "var"
        self.a = value
        self.r = name
        self.c = const
        self.line = self.b and self.a
        self.expr = "{0} {1} {2}".format(self.b, self.r, self.a)
        vars.update({"{0}".format(self.r): (self.a, self.c)})
        return True
        
    def fixvar(self, init):
        self.b = "fvar"
        self.a = value
        self.r = name
        self.c = const
        self.line = self.b and self.a
        self.expr = "{0} {1} {2}".format(self.b, self.r, self.a)
        vars.update({"{0}".format(self.r): (self.a, self.c)})
        return True


    def ampersand(self, init):
        self.line = line
        self.r = self.a, "&", self.b
        self.line = self.r
        self.expr = "{0} {1}".format(self.r, self.a)
        return True

    
    def log(self, init):
        self.a = "("
        self.b = ")"
        self.r = line
        self.expr = "log{0}{1}{2}".format(self.a, self.r, self.b)
        print(self.r and self.expr)
        return True
        """
        if self.a == str:
            print(self.r)
        elif self.a == "true" or self.a == "false":
            print(self.r)
        else:
            print(float(self.r))
        return self.expr 
        """

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
        


""""""
type_inst = type()
math_inst = math()
ops_inst = operands()

def interpret(expr):
    methods = {
    # Key
    "parentheses": ops_inst.parentheses,
    "comment": ops_inst.comment,
    "ampersand": ops_inst.ampersand,
    "bool": type_inst.typebool,
    "int": type_inst.typenum,
    "str": type_inst.typestr,


    # Math
    "add": math_inst.add,
    "sub": math_inst.sub,
    "div": math_inst.div,
    "mul": math_inst.mul,
    "floordiv": math_inst.floordiv,
    "remainder": math_inst.remainder,
    "line": math_inst.entry,

    # Operands
    "log()": ops_inst.log,
    "var": ops_inst.regvar,
    "fvar": ops_inst.fixvar,
    }
    ops_inst.log(any)
    """ 
     for line in methods:
        # print("method:", line)
        a = any
        methods[line](a)
        print(ops_inst.log(a))

    return False 
    for line in contents:
        for line in methods:
            return methods
        else:
            return False
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
    """

def execute():
    print("Starting..")
    with open(testscript, "r") as f:
        for script_line in f:
            print(script_line.rstrip())
            interpret(script_line)
execute()
