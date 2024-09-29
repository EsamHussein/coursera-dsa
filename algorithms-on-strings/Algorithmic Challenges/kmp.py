# python3
import sys


def compute_prefix_function(pattern):
    s = [0] * len(pattern)
    border = 0

    for i in range(1, len(pattern)):
        while (border > 0) and (pattern[i] != pattern[border]):
            border = s[border - 1]
        border = border + 1 if pattern[i] == pattern[border] else 0
        s[i] = border

    return s


def find_pattern(pattern, text):
    S = f'{pattern}${text}'
    s = compute_prefix_function(S)
    p = len(pattern)

    return [i - 2 * p for i in range(p + 1, len(S)) if s[i] == p]


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
