#! /usr/bin/env python3
'''search'''


def search(sequeue, num):
    sequenue_len = len(sequeue)
    if sequenue_len <= 1:
        return sequeue

    new_queue = sorted(sequeue)
    middle = sequenue_len // 2
    middle_val = new_queue[middle]

    if middle_val > num:
        result = search(new_queue[:middle], num)
    elif middle_val < num:
        result = search(new_queue[middle:], num)
    elif middle_val == num:
        result = middle
    else:
        result = None

    return result


a = [1, 3, 5, 6]
print(search(a, 5))
print(search(a, 3))
