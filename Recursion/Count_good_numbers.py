
def count_good_numbers(number):
    weight = 4 if number % 2 == 0 else 5
    if number == 1 : return 5
    return weight * count_good_numbers(number-1)

print(count_good_numbers(3))

