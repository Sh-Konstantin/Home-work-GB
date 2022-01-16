srs = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([srs[i] for i in range(len(srs)) if srs[i] not in srs[i+1:] and srs[i] not in srs[:i]])
#result = [23, 1, 3, 10, 4, 11]