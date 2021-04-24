while True:
    s = input("Знак (+,-,*,/, ілі нуль для завершения): ")
    if s == '0': break
    if s in ('+','-','*','/'):
        x = int(input("x="))
        y = int(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Делить на нуль нельзя!")
    else:        
        print("Неверный знак операции!")
