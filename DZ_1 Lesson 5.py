def odd_nums (n):
    for i in range(1,n+1,2):
        yield i
odd_to_11 = odd_nums(11)
print(next(odd_to_11))
print(next(odd_to_11))
print(next(odd_to_11))
print(next(odd_to_11))
print(next(odd_to_11))
print(next(odd_to_11))
