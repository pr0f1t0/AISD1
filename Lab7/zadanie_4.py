from Lab7.stack import Stack


def operacje(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        try:
          return a / b
        except:
            print("Dzielenie przez 0!")
    elif op == "^":
        return a ** b


def oblicz(wyraz):
    l_st = Stack()
    l_list = wyraz.split()

    for i in l_list:
        if i in '0123456789':
            l_st.push(float(i))
        else:
            a = l_st.pop()
            b = l_st.pop()
            c = operacje(b, a, i)
            l_st.push(c)

    return l_st.pop()


print(oblicz('7 3 + 5 2 - 2 ^ *'))







