stroka1 = input()
stroka2 = input()
for symbol in stroka2:
    if symbol in stroka1:
        stroka1 = stroka1.replace(symbol, '', 1) 
    else:
        print(symbol)
        break
