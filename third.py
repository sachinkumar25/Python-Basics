list1 = [2,34,5,212]
def listmultiply(product):
    x = 1
    for i in product:
        x = x * i
    return x

multiply = listmultiply(list1)
print(multiply)
