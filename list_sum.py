demolist =[1,89, 23.4, 100, "23%", 92, "88A"]


def get_total_value(list):
    i = 0
    for num in list:
        if isinstance(num, (int, float)):
            i += num
    return i

answer_2 = get_total_value(demolist)
print(answer_2)
