operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
}


def calc(expr):
    a, op, b = expr.split()
    return operations[op](eval(a), eval(b))


assert calc('2 + 2') == 4
assert calc('2 - 2') == 0
assert calc('2 - 0.2') == 1.8

try:
    calc('2 * 2') == 4
except KeyError:
    pass
else:
    raise RuntimeError("Should raise KeyError because there is no operation *")

operations['*'] = lambda a, b: a * b

# now verifying that new operation was added
assert calc('2 * 2') == 4
