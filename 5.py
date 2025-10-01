#задача 5
def vnesh(tp):
    def vnutr(stroka):
        nums = list(map(int, stroka.split()))
        if tp == 'list':
            return nums
        else:
            return tuple(nums)
    return vnutr


tp = input()
posledovatelnost = input()

lst = vnesh(tp)(posledovatelnost)
print(lst)
