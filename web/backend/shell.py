
import Lib.Lexer as lx

#* shell returns us the Result, Error
def shell(text):
    if text.strip() == "": 
        return None, None

    result, error = lx.runLexer('<stdin>' , text)

    if error: 
        return None, error.toStr()
    elif result:
        return result, None
        #print(repr(result))

def removeYazdir(string):
    i = 0 
    finalStr = ''

    while i < len(string):
        if string[i] == 'y' and string[i+1] == 'a':
            i = i + 6
        finalStr += string[i]
        i = i + 1

    return finalStr

def fixIf(string):
    i = 0 
    input = removeYazdir(string)
    l = list(input)

    while i < len(input):    
        if input[i-1] != 'e' and input[i] == 'i' and input[i+1] == 'f':
            endIndex = input.find('end',i,len(input))
            subStr = input[i:endIndex]
            subStr = subStr.replace('\n', '')
            subStr = subStr.replace('end', '')
            subStr = subStr.replace(';', '')
            l[i:len(input)] = subStr
        i = i + 1

    ret = "".join(str(x) for x in l)
    return ret