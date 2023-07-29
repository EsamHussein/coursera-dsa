# Uses python3
import sys


def get_majority_element(a):
    count, possible_element = 0, None
    for num in a:
        if count == 0:
            possible_element = num
            count += 1
        elif num == possible_element:
            count += 1
        else:
            count -= 1

    count = sum(1 for num in a if num == possible_element)
    return possible_element if count > len(a) / 2 else -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
