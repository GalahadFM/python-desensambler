# ADD, SUB, MUL, DIV , PUSH, POP, INC , DEC, CMP, JE, JNE

# Ax, Bx, Cx, Dx, Sp, Bp, SI, BI
var = {'Ax': 5, 'Bx': 2, 'Cx': 0, 'Dx': 0, 'Sp': 0, 'Bp': 0, 'Si': 0, 'Bi': 0}
stack = []


def functions(name, a, b):
    if name == 'MOV':
        mov(a,b)
    if name == 'ADD':
        add(a, b)
    if name == 'DIV':
        div(a)
    if name == 'MUL':
        mul(a)
    if name == 'SUB':
        sub(a, b)
    if name == 'PUSH':
        push(a)
    if name == 'POP':
        pop()


def mov(x, b): var[x] = int(b)


def add(x, b): var[x] = var.get(x) + var.get(b)


def mul(b): var['Ax'] = var.get('Ax') * var.get(b)


def div(b):
    var['Dx'] = var.get('Ax') % var.get(b)
    var['Ax'] = int(var.get('Ax') / var.get(b))


def sub(x, b): var[x] = var.get(x) - var.get(b)


def push(a): stack.append(a)


def pop(): stack.pop()


def inc(x): var[x] = var.get(x) + 1


def dec(x): var[x] = var.get(x) - 1


def com(a, b): return a == b


if __name__ == '__main__':
    pass
