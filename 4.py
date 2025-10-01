#задача 4
def vnesh(tag):
    def vlozh(stroka):
        print(f"<{tag}>{stroka}</{tag}>", sep="")
    return vlozh


tg = input()
slovo = input()
a = vnesh(tg)
a(slovo)
