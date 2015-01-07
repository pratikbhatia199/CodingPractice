__author__ = 'pratik'

from collections import deque
class GraphBFS:


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
    set_visited = set()
    set_visiting = set()
    def bfs(self, queue):
        root = queue.popleft()

        for adj_node in self.dict_graph[root]:
            if adj_node not in self.set_visiting:
                if adj_node not in self.set_visited:
                    self.set_visiting.add(adj_node)
                    queue.append(adj_node)
        print root
        self.set_visited.add(root)

    """
    dict_graph = {'u':['v','x'],
              'v':['y'],
              'w':['z','y'],
              'x':['v'],
              'y':['x'],
              'z':['z']
              }
    """


    # def bfs(self, node):
    #         print node
    #         self.set_visited.add(node)
    #         for adj_value in self.dict_graph[node]:
    #             if adj_value not in self.set_visited:
    #                 if adj_value not in self.queue:
    #                     self.queue.append(adj_value)
    #
    #         while(self.queue):
    #             node = self.queue.popleft()
    #             self.bfs(node)


def main():
    g_bfs = GraphBFS()

    queue = deque()
    queue.append('u')
    while(queue):
        g_bfs.bfs(queue)


main()