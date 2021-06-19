def getMissingNo(numbers):
    n = len(numbers)
    sum_of_total = sum(numbers)
    total = (n+1)*(n+2)/2
    return int(total - sum_of_total)


numbers = [1,3,4,2,6,8,5]
print(getMissingNo(numbers))