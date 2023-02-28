import re

file = open("read.py")

operators = {'=' : 'operator','+' : 'operator','-' : 'operator','/' : 'operator','==' : 'operator','%' : 'operator'
,'*' : 'operator','<' : 'operator','>' : 'operator' }
operators_key = operators.keys()

keyword = ['for','while','False','await','else','if','import','pass','None','break','except','in','raise','True'
,'class','finally','is','return','and','continue','lambda','try','as','def','from','nonlocal','assert','del'
,'global','not','with','async','elif','or','yield','whileend','forend','ifend','range','print']

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma' }
punctuation_symbol_key = punctuation_symbol.keys()

seperator = { '(' : 'seperator', ')' : 'seperator',' ':'space' }
seperater_key = seperator.keys()

dataFlag = False

a=file.read()

program = a.split("\n")
print("token ---------- lexems\n")
for line in program:
    tokens=line.split(' ')
    for token in tokens:
        if token in operators_key:
            print(token ,"----------", operators[token])
        elif token in keyword:
            print(token ,"---------- keyword")
        elif token in punctuation_symbol_key:
            print (token ,"----------", punctuation_symbol[token])
        elif token in seperater_key:
            print (token ,"----------", seperator[token])
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