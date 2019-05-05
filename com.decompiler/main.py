
# ADD, SUB, MUL, DIV , PUSH, POP, INC , DEC, CMP, JE, JNE

# Ax, Bx, Cx, Dx, Sp, Bp, SI, BI
var = {'AX': 0, 'BX': 0, 'CX': 0, 'DX': 0, 'SP': 0, 'BP': 0, 'SI': 0, 'BI': 0}
stack = []
index = 0
last_index = 0
jump_points = {}
instructions = open('test02.txt', 'r').readlines()
comparison = None


def execFunction(name, v):

    global index
    global last_index

    if name == 'MOV' or name == "mov":
        mov(v[0], v[1])
    if name == 'SUM' or name == "sum":
        add(v[0], v[1])
    if name == 'DIV' or name == "div":
        div(v[0])
    if name == 'MUL' or name == "mul":
        mul(v[0])
    if name == 'SUB' or name == "sub":
        sub(v[0], v[1])
    if name == 'PUSH' or name == "push":
        push(v[0])
    if name == 'POP' or name == "pop":
        POP()
    if name == 'CMP' or name == "cmp":
        cmp(v[0], v[1])
    if name == 'INC' or name == "inc":
        inc(v[0])
    if name == 'DEC' or name == "dec":
        dec(v[0])


def mov(x, b): var[x] = int(b)


def add(x, b): var[x] = var.get(x) + int(b)


def mul(b): var['AX'] = var.get('AX') * var.get(b)


def div(b):
    if b == 0:
        print("Unsupported Operand")
    else:
        var['DX'] = var.get('AX') % var.get(b)
        var['AX'] = int(var.get('AX') / var.get(b))


def sub(x, b): var[x] = var.get(x) - var.get(b)


def push(a): stack.append(var.get(a))


def POP():
    global stack
    if len(stack) > 0:
        stack.pop()


def inc(x): var[x] = var.get(x) + 1


def dec(x): var[x] = var.get(x) - 1


def cmp(x, b):
    global comparison
    comparison = (var.get(x) == int(b))


def read_operation(l):
    l = l.strip()
    return l.split(' ')[0]


def read_variables(l):
    if ',' in l:
        return l.strip().split(' ')[1].split(',')
    return [l.strip().split(' ')[-1].strip()]


def has_line_jp(l, i):
    if ':' in l:
        jump_points.update({line.split(':')[0]: i})


def jmp(new_index):
    global index
    global last_index
    last_index = index
    index = new_index


def is_line_jp(l):
    return ':' in l


def save_jp(l, i):
    global jump_points
    jump_points.update({l.split(':')[0]: i})


def read_jp():
    global instructions
    for x in range(len(instructions)):
        if is_line_jp(instructions[x]):
            save_jp(instructions[x], x)


def is_in_jp(name):
    return jump_points.get(name) is not None


def is_a_jp(op):
    return op == 'JE' or op == 'JNE' or op == 'JUM' or op == 'JMP'


def is_a_tag(op):
    key_list = jump_points.keys()
    for key in key_list:
        if key == op: return True
    return False


def read_instruction_line(op, va):
    global index
    global comparison
    if is_a_jp(op):
        return change_index_on_jp(op, va)
    execFunction(op, va)


def change_index_on_jp( op, va):

    global index
    global comparison
    if op == 'JUM' or op == 'JMP':
        index = (jump_points.get(va[0]) - 1)
        return
    elif op == 'JE' and comparison:
        index = (jump_points.get(va[0]) - 1)
    elif op == 'JNE' and not comparison:
        index = (jump_points.get(va[0]) - 1)
    return


def is_blank_line():
    return instructions[index].strip() == ''


def read_instructions_line(line):
    return read_operation(line), read_variables(line)


if __name__ == '__main__':
    read_jp()
    iter = 0
    while index < len(instructions):
        if not is_blank_line():
            operation = read_operation(instructions[index].strip())
            if is_a_tag(operation.split(':')[0]):
                line = instructions[index].strip().split(':')[1]
                operation, variables = read_instructions_line(line)
                if operation == 'RET' or variables[0] == 'RET': break
                read_instruction_line(operation, variables)
            else:
                operation, variables = read_instructions_line(instructions[index].strip())
                if operation == 'RET' or variables[0] == 'RET': break
                read_instruction_line(operation, variables)
        index += 1

    print('Variables = ', var)
    print('Stack = ', stack)
