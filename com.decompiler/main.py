# ADD, SUBS, MUL, DIV , PUSH, POP, INC , DEC, CMP ,NMP , JE, JNE

# Ax, Bx, Cx, Dx, Sp, Bp, SI, BI

variables = {'Ax' : 0, 'Bx' : 0,'Cx' : 0,'Dx' : 0,'Sp' : 0,'Bp' : 0,'Si' : 0,'Bi' : 0}

def mov(x, b):
    variables[x] = b


if __name__ == '__main__':
    mov('Ax', 2)
    print(variables.get('Ax'))
