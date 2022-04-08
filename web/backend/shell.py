
import Lib.Lexer as lx

#* shell returns us the Result, Error
def shell(text):
    return text, None
    if text.strip() == "": 
        return None, None

    result, error = lx.runLexer('<stdin>' , text)

    if error: 
        return None, error.toStr()
    elif result:
        return result, None
        #print(repr(result))