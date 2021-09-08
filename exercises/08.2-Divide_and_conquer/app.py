list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list(param1):
    odd = []
    even = []
    final_list = []
    for a in param1:
        if a % 2 != 0:
            odd.append(a)
        else:
            even.append(a)
    final_list.append(odd)
    final_list.append(even)
    return final_list

print(merge_two_list(list_of_numbers))

