def lexer(num):
    int_real_FSM(num)


def int_real_FSM(num):
    states = {
        'start': [('123456789', 'integer'), ('0', 'zero')],
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
            if state == 'zero':
                state = 'integer'
            if state != 'integer' and state != 'real':
                state = 'error'
            break
    # return state
    print(state)


if __name__ == '__main__':
    nums = ['0', '5.67', '33468', '-8', '01', '67a8', '_76432', '546.42.5', '6865.453', '5.']
    for num in nums:
        lexer(num)