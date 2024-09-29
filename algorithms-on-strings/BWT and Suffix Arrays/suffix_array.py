# python3
import sys


def build_suffix_array(text):
    suffixes = [(i, text[i:]) for i in range(len(text))]
    suffixes = sorted(suffixes, key=lambda t: t[1])

    return [suffixes[i][0] for i in range(len(suffixes))]


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
