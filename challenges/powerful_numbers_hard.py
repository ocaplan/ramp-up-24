def powerful_numbers(num):
    prime_factors = set()
    divisor = 2
    copy_of_num = num
    while divisor <= copy_of_num:
        if copy_of_num % divisor == 0:
            prime_factors.add(divisor)
            copy_of_num /= divisor
        else:
            divisor += 1
    for prime_factor in prime_factors:
        if num % prime_factor ** 2 != 0:
            return False
    return True