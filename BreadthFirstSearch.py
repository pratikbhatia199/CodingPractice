__author__ = 'pratik'

from collections import deque
class GraphBFS:

    set_visited = set()
    queue = deque()

    dict_graph = {'r':['s', 'v'],
                  's':['r', 'w'],
                  't':['u', 'w', 'x'],
                  'u':['t', 'y'],
                  'v':['r'],
                  'w':['s', 't', 'x'],
                  'x':['w', 't', 'y'],
                  'y':['x', 'u']
                  }

    def bfs(self, node):
            print node
            self.set_visited.add(node)
            for adj_value in self.dict_graph[node]:
                if adj_value not in self.set_visited:
                    if adj_value not in self.queue:
                        self.queue.append(adj_value)

            while(self.queue):
                node = self.queue.popleft()
                self.bfs(node)


def main():
    g_bfs = GraphBFS()
    g_bfs.bfs('s')

main()