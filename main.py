import sys
operators = {'=' : 'operator','+' : 'operator','-' : 'operator','/' : 'operator','==' : 'operator','%' : 'operator'
,'*' : 'operator','<' : 'operator','>' : 'operator', '<=' : 'operator', '>=' : 'operator', '+=' : 'operator',
'-=': 'operator'}
operators_key = operators.keys()

keyword = ['for','while','False','await','else','if','import','pass','None','break','except','in','raise','True'
,'class','finally','is','return','and','continue','lambda','try','as','def','from','nonlocal','assert','del'
,'global','not','with','async','elif','or','yield','endwhile','forend','ifend','range','print']


punctuation_symbol = { ':' : 'separator', ';' : 'separator', '.' : 'separator' , ',' : 'separator' }
punctuation_symbol_key = punctuation_symbol.keys()

separator = { '(' : 'separator', ')' : 'separator',' ':'space' }
separator_key = separator.keys()

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


if __name__ == '__main__':
    fname = input('Enter the input file name: ')
    file = open(fname)
    oname = input('Enter the output file name: ')
    sys.stdout = open(oname, "w")
    a=file.read()
    program = a.split("\n")
    print("lexems ---------- token\n")
    for line in program:
        tokens = line.split(' ')
        for token in tokens:
            if token in operators_key:
                print(token ,"----------", operators[token])
            elif token in keyword:
                print(token ,"---------- keyword")
            elif token in punctuation_symbol_key:
                print (token ,"----------", punctuation_symbol[token])
            elif token in separator_key:
                print (token ,"----------", separator[token])
            else:
                if (id_FSM(token) != 'error'):
                    print(token, "---------- identifier")
                elif (int_real_FSM(token) != 'error'):
                    print(token, "----------", int_real_FSM(token))
                else:
                    print (token ,"---------- invalid")
    sys.stdout.close()