# returns the nth value in the fibonacci series
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 2) + fibonacci(num - 1)


# returns the nth value in the lucas numbers
def lucas(num):
    if num == 0:
        return 2
    elif num == 1:
        return 1
    else:
        return lucas(num - 2) + lucas(num - 1)


# returns the fibonacci sequence, lucas sequence, or a completely new sequence based on the input
def sum_series(num, first_num=0, second_num=1):
    if num == 0:
        return first_num
    elif num == 1:
        return second_num
    else:
        return sum_series(num - 1, first_num, second_num) + sum_series(num - 2, first_num, second_num)
