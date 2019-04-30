# ADD, SUB, MUL, DIV , PUSH, POP, INC , DEC, CMP, JE, JNE

# Ax, Bx, Cx, Dx, Sp, Bp, SI, BI
var = {'AX': 0, 'BX': 0, 'CX': 0, 'DX': 0, 'SP': 0, 'BP': 0, 'SI': 0, 'BI': 0}
stack = []
index = 0
last_index = 0
jump_points = {}
instructions = open('test02.txt', 'r').readlines()


def execFunction(name, v):
    if name == 'MOV':
        mov(v[0], v[1])
    if name == 'ADD':
        add(v[0], v[1])
    if name == 'DIV':
        div(v[0])
    if name == 'MUL':
        mul(v[0])
    if name == 'SUB':
        sub(v[0], v[1])
    if name == 'PUSH':
        push(v[0])
    if name == 'POP':
        pop()


def mov(x, b): var[x] = int(b)


def add(x, b): var[x] = var.get(x) + var.get(b)


def mul(b): var['AX'] = var.get('AX') * var.get(b)


def div(b):
    var['DX'] = var.get('AX') % var.get(b)
    var['AX'] = int(var.get('AX') / var.get(b))


def sub(x, b): var[x] = var.get(x) - var.get(b)


def push(a): stack.append(var.get(a))


def pop(): stack.pop()


def inc(x): var[x] = var.get(x) + 1


def dec(x): var[x] = var.get(x) - 1


def com(a, b): return a == b


def readInstructions(filename):
    file = open(filename, 'r')
    return file.readlines()


def readOperation(line):
    line = line.strip()
    return line.split(' ')[0]


def readVaraibles(line):
    if ',' in line:
        return line.strip().split(' ')[1].split(',')
    return [line.strip().split(' ')[1]]


def has_line_jp(line, index):
    if ':' in line:
        jump_points.update({line.split(':')[0]: index})


def jmp(new_index):
    global index
    global last_index
    last_index = index
    index = new_index


def is_line_jp(line):
    return ':' in line


def save_sp(line, index):
    jump_points.update({line.split(':')[0]: index})


if __name__ == '__main__':
    print('yeeey')
    print(instructions)
    # instructions = readInstructions('test02.txt')

    while index < len(instructions):
        # if instructions[index].strip() == '':
        #     continue
        line = instructions[index].strip()
        print(line)
        if line.strip() == '':
            continue
        # if '\n' in line:
        #     print('blank line')
        # # if is_line_jp(line):
        # #     save_sp(line, index)
        # #     line = line.split(':')[1]
        #
        # execFunction(readOperation(line), readVaraibles(line))
        index += 1

    print(var)
    print(stack)
    # arr = readInstructions('test01.txt')
    # print(arr)