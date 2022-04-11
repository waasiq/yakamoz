
import Lib.Lexer as lx

while (True):
    text = input('yakamoz >>> ')
    if text.strip() == "": continue
    result, error = lx.runLexer('<stdin>' , text)

    if error: print(error.toStr())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
           print(repr(result))