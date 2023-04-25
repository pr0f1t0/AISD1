from Lab7.stack import Stack


def parChecker(symbolString):
    s = Stack() #definicja nowego stosu
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


print(parChecker('((()))'))
print(parChecker('((())'))
print(parChecker('((())))))'))

