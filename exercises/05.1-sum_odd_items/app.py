arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]
def sumOdds(param1):
    total = 0
    for num in param1:
        if num % 2 != 0:
            total += num
    print(total)
sumOdds(arr)