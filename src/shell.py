import Lexer as lx 

while (True):
    text = input('yakamoz >>> ')
    result, error = lx.runLexer('<stdin>' , text)

    if error: print(error.toStr())
    else: print(result)