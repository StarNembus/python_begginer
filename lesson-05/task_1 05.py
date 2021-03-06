def odd_nums(n):
    for num in range(0, n + 1):
        if num % 2 == 1:
            yield num


nums = odd_nums(16)
print(*nums)
