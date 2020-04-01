add_list = [12,123,1234,543]

def list_addition(input1):
    addition = 0
    for i in input1:
        addition = addition + i
    return addition

result = list_addition(add_list)
print(result)
