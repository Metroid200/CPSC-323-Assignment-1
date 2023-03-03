def lexer(num):
    id_FSM(num)


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
    # return state
    print(state)


if __name__ == '__main__':
    ids = ['kjsh_0', 'hcwcb', '0cjsc', '_fjd2', 'Ad', 'hcuFBJ1C_']
    for id in ids:
        lexer(id)