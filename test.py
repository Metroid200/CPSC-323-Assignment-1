def lexer(num):
    int_real_FSM(num)

def int_real_FSM(num):
    states = {
        "START": [("123456789", "INTEGER*"), ("0", "ZERO*")],
        "INTEGER*": [("0123456789", "INTEGER*"), (".", "DOT")],
        "ZERO*": [(".", "DOT")],
        "DOT": [("0123456789", "SIGNIFICAND*")],
        "SIGNIFICAND*": [("0123456789", "SIGNIFICAND*")]
    }
    # print(states)
    state = "START"
    while True:
        if (len(num) > 0):
            # print("Current state: " + state)
            token = num[0]
            num = num[1:]
            found = False
            for v in states[state]:
                if token in v[0]:
                    state = v[1]
                    found = True
                    break
            if not found:
                state = "ERROR"
        else:
            if "*" not in state:
                state = "ERROR"
            break
    print(state)


if __name__ == '__main__':
    num = "0.0"
    lexer(num)