list1 = [12,13,14,15,16,17]

def evenout(input1):
    even = []
    for i in input1:
        if i % 2 == 0:
            even.append(i)
    return even

result = evenout(list1)
print(result)
