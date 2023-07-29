# python3

import sys
import threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.nodes = {i: [] for i in range(self.n)}
        for i in range(self.n):
            if self.parent[i] != -1:
                self.nodes[self.parent[i]] += [i]

    def compute_height(self):
        root = None
        try:
            root = self.parent.index(-1)
        except ValueError:
            return 0
        queue = [root]
        height = 0

        while True:
            node_count = len(queue)
            if node_count == 0:
                return height
            height += 1
            while node_count > 0:
                node = queue[0]
                queue.pop(0)
                if self.nodes[node]:
                    queue.extend(iter(self.nodes[node]))
                node_count -= 1


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()
