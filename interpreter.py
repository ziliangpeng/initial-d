from errors import *
import re
from operator import sub, add, mul


OPERATORS = {
    '*': mul,
    '+': add,
    '-': sub,
}


class Calculator(object):
    RE_INT = '[-+]?([1-9]\d*|0)'

    RE_VAR = '[_a-zA-Z][_a-zA-Z0-9]*'

    RE_RETURN = 'return\s+(?P<var>%s)' % RE_VAR

    RE_ARITHMETIC = '(?P<opl>%s)\s*(?P<op>(\+|\-|\*))\s*(?P<opr>%s)' % (RE_VAR, RE_VAR)

    RE_ASSIGN = '(?P<lhs>%s)\s*\=\s*(?P<rhs>(%s|%s|%s))' % (RE_VAR, RE_INT, RE_VAR, RE_ARITHMETIC)

    def __init__(self):
        self.mem_table = {}

    def run(self, line):
        if re.fullmatch(self.RE_ASSIGN, line):  # is assignment statement
            self.do_assignment(line)
        elif re.fullmatch(self.RE_RETURN, line):  # is return statement
            return self.do_return(line)
        else:
            raise InvalidStatementException()

    def do_assignment(self, line):
        match = re.fullmatch(self.RE_ASSIGN, line)
        lhs = match.group('lhs')
        rhs = match.group('rhs')
        self._assign(lhs, self._resolve(rhs))

    def do_return(self, line):
        match = re.match(self.RE_RETURN, line)
        var = match.group('var')
        return self._lookup(var)

    def _resolve(self, stmt):
        if re.fullmatch(self.RE_INT, stmt):
            return int(stmt)
        elif re.fullmatch(self.RE_VAR, stmt):
            return self._lookup(stmt)
        else:
            match = re.fullmatch(self.RE_ARITHMETIC, stmt)
            if match:
                opl = match.group('opl')  # operand on left
                op = match.group('op')  # operator
                opr = match.group('opr')  # operand on right
                return OPERATORS[op](self._lookup(opl), self._lookup(opr))
            else:
                raise InvalidStatementException()

    def _lookup(self, var):
        if var in self.mem_table:
            return self.mem_table[var]
        else:
            raise VariableNotDefined()

    def _assign(self, var, value):
        self.mem_table[var] = value


def interpret(program):
    program = program.strip().split('\n')
    program = map(str.strip, program)

    c = Calculator()
    for line in program:
        r = c.run(line)
        if r:
            # return on the first return statement. following statements will be ignored.
            return r

    raise NoReturnExceptioon()
