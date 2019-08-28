
import gen_program
from gen_program import Node
import random
import gen_inputs

MathFunctions = [
                 "acos(double)",
                 "asin(double)",
                 "atan(double)",
                 "atan2(double,double)",
                 "cos(double)",
                 "cosh(double)",
                 "sin(double)",
                 "sinh(double)",
                 "tanh(double)",
                 "exp(double)",
                 "ldexp(double,int)",
                 "log(double)",
                 "log10(double)",
                 "pow(double,double)",
                 "sqrt(double)",
                 "ceil(double)",
                 "fabs(double)",
                 "floor(double)",
                 "fmod(double,double)"
                 ]

class MathExpression(Node):
    def __init__(self, code="", left=None, right=None):
        self.code = code
        self.left  = left
        self.right = right
        self.parameters = []

        i = random.randrange(0, len(MathFunctions))
        func = MathFunctions[i]
        #print("Found", func)
        self.code = func.split("(")[0]
        
        types = func[:-1].split("(")[1].split(",")
        #print("Types:", types)
        for t in types:
            if t == "double":
                if gen_program.lucky():
                    self.parameters.append( gen_inputs.InputGenerator().genInput() )
                else:
                    self.parameters.append(gen_program.Expression())
            elif t == "int":
                self.parameters.append("2")

    def printCode(self):
        params = []
        for p in self.parameters:
            if isinstance(p, str):
                params.append(p)
            else:
                params.append(p.printCode(False))
        ret = self.code + "(" + ", ".join(params) + ")"
        return ret

if __name__ == "__main__":
    m = MathExpression()
    print(m.printCode())