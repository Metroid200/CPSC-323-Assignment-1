import re

file = open("read.py")

lexstates = ["Identifier", "Integer", "Real", "Null"]
operators = {'=' : 'operator','+' : 'operator','-' : 'operator','/' : 'operator','==' : 'operator','%' : 'operator'
,'*' : 'operator','<' : 'operator','>' : 'operator' }
operators_key = operators.keys()

keyword = ['for','while','False','await','else','if','import','pass','None','break','except','in','raise','True'
,'class','finally','is','return','and','continue','lambda','try','as','def','from','nonlocal','assert','del'
,'global','not','with','async','elif','or','yield','endwhile','forend','ifend','range','print']

integer = ["0", "1", "2", "3", "4", "5","6", "7", "8", "9"]

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma' }
punctuation_symbol_key = punctuation_symbol.keys()

separator = { '(' : 'separator', ')' : 'separator',' ':'space' }
separator_key = separator.keys()

dataFlag = False

a=file.read()


###### Start of FSM build attempt, delete block if inoperable #########
class myFSM:
    def __init__(self):
        self.handlers = {}
    def add_state(self, name, handler):
        self.handlers[name] = handler
    def run(self, startingState, cargo):
        handler = self.handlers[startingState]
        while True:
            (newState, cargo) = handler(cargo)
            if newState == "END":
                print ("END reached")
                break
            handler = self.handlers[newState]
    def state_id(cargo):
        pass
    def state_int(cargo):
        pass
    def state_real(cargo):
        pass
lexer = myFSM()
lexer.add_state("Identifier", state_id)
lexer.add_state("Integer", state_int)
lexer.add_state("Real", state_real)


#lexer.run("Identifier", 3)

######### end of FSM build attempt #############
program = a.split("\n")
print("lexems ---------- token\n")
for line in program:
    tokens=line.split(' ')
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
            try:
                variable = int(token)
                variable = float(token)
            except ValueError:
                variable = None
            if variable:
                print (token ,"---------- real")
            elif token == ' ':
                pass
            else:
                print (token ,"---------- identifier")
 
    dataFlag=False
