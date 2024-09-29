# python3
import sys


def build_trie(patterns):
    tree = {0: {}}
    index = 1

    for pattern in patterns:
        current = tree[0]
        for letter in pattern:
            if letter in current.keys():
                current = tree[current[letter]]
            else:
                current[letter] = index
                tree[index] = {}
                current = tree[index]
                index = index + 1
    return tree


def solve(text, n, patterns):
    trie = build_trie(patterns)

    n = len(text)
    return [i for i in range(n) if prefix_trie_matching(text[i:], trie)]


def prefix_trie_matching(text, trie):
    idx = 0
    symbol = text[idx]
    current = trie[0]

    while True:
        if not current:
            return True
        elif symbol in current.keys():
            current = trie[current[symbol]]
            idx = idx + 1
            symbol = text[idx] if idx < len(text) else '@'
        else:
            return False


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    patterns = [sys.stdin.readline().strip() for _ in range(n)]
    ans = solve(text, n, patterns)
    sys.stdout.write(' '.join(map(str, ans)) + '\n')
