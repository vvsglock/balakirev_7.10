#задача 1
def counter_add():
    def add_5(num):
        return num + 5
    return add_5

cnt = counter_add()
k = int(input())
print(cnt(k))
