def find_max(numbers):
    maxnum = numbers[0]
    for num in numbers:
        if num > maxnum:
            maxnum = num
    return maxnum    
numbers = [13,42,17]
print(find_max(numbers))
