#задача 3
def vnesh():
    def vnutr(stroka):
        print(f"<h1>{stroka}</h1>")
    return vnutr


slovo = input()
a = vnesh()
a(slovo)
