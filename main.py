import sys


# List of operators, unsure if => is a typo so >= is also included
operators = {'=': 'operator', '+': 'operator', '-': 'operator', '/': 'operator', '==': 'operator',
             '*': 'operator', '<': 'operator', '>': 'operator', '<=': 'operator', '=>': 'operator',
             '>=': 'operator', '!=': 'operator'}
operators_key = operators.keys()

# List of keywords
keyword = ['function', 'int', 'bool', 'real', 'if', 'fi', 'else', 'return', 'put', 'get', 'while', 'endwhile',
           'true', 'false']

# List of separators
separator = {'(' : 'separator', ')' : 'separator', '#': 'separator', ':' : 'separator', ';' : 'separator',
             ');' : 'separator' , ',' : 'separator', '{' : 'separator', '}' : 'separator', '|': 'separator'}
separator_key = separator.keys()


# Ignore comments found in file
def ignore_comment(str):
    result = ''
    skip = 0
    for i in range(len(str)):
        if str[i] == '[' and str[i + 1] == '*':
            skip += 1
        elif str[i - 1] == '*' and str[i] == ']':
            skip -= 1
        elif skip == 0:
            result += str[i]
    return result


# Identifier FSM
def id_FSM(id):
    states = {
        'start': [('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'letter')],
        'letter': [('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'letter'), ('0123456789', 'integer'), ('_', 'underscore')],
        'integer': [('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'letter'), ('0123456789', 'integer'), ('_', 'underscore')],
        'underscore': [('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'letter'), ('0123456789', 'integer'), ('_', 'underscore')],
    }
    state = 'start'
    while True:
        if (len(id) > 0):
            token = id[0]
            id = id[1:]
            found = False
            for v in states[state]:
                if token in v[0]:
                    state = v[1]
                    found = True
                    break
            if not found:
                state = 'error'
                break
        else:
            if state != 'letter' and state != 'integer' and state != 'underscore':
                state = 'error'
            break
    return state


# Integer and Real FSM
def int_real_FSM(num):
    states = {
        'start': [('0123456789', 'integer')],
        'integer': [('0123456789', 'integer'), ('.', 'dot')],
        'zero': [('.', 'dot')],
        'dot': [('0123456789', 'real')],
        'real': [('0123456789', 'real')]
    }
    state = 'start'
    while True:
        if (len(num) > 0):
            token = num[0]
            num = num[1:]
            found = False
            for v in states[state]:
                if token in v[0]:
                    state = v[1]
                    found = True
                    break
            if not found:
                state = 'error'
                break
        else:
            if state != 'integer' and state != 'real':
                state = 'error'
            break
    return state


# Lexer function
def lexer(token):
    if token == '':
        return
    if token in operators_key:
        print(token ,"----------", operators[token])
    elif token in keyword:
        print(token ,"---------- keyword")
    elif token in separator_key:
        print(token ,"----------", separator[token])
    else:
        if (id_FSM(token) != 'error'):
            print(token, "---------- identifier")
        elif (int_real_FSM(token) != 'error'):
            print(token, "----------", int_real_FSM(token))
        else:
            print(token ,"---------- invalid")


if __name__ == '__main__':
    fname = input('Enter the input file name: ')
    file = open(fname)
    oname = input('Enter the output file name: ')
    sys.stdout = open(oname, "w")
    a=file.read()
    a=ignore_comment(a)
    program = a.split("\n")
    print("lexeme ---------- token\n")
    for line in program:
        tokens = line.split(' ')
        for token in tokens:
            lexer(token)
    sys.stdout.close()