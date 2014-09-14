__author__ = 'pratik'
from collections import deque

class GraphBFS:

    set_visited = set()
    queue = deque()
    """
    dict_graph = {'r':['s', 'v'],
                  's':['r', 'w'],
                  't':['u', 'w', 'x'],
                  'u':['t', 'y'],
                  'v':['r'],
                  'w':['s', 't', 'x'],
                  'x':['w', 't', 'y'],
                  'y':['x', 'u']
                  }
    """
    dict_parent = { }


    dict_graph = {'u':['v','x'],
              'v':['y'],
              'w':['z','y'],
              'x':['v'],
              'y':['x'],
              'z':['z']
              }



    def bfs(self, node):
            print node
            self.set_visited.add(node)
            for adj_value in self.dict_graph[node]:
                if adj_value not in self.set_visited:
                    if adj_value not in self.queue:
                        self.dict_parent[adj_value]=node
                        self.queue.append(adj_value)

            while(self.queue):
                node = self.queue.popleft()
                self.bfs(node)

    def bfs_path(self, node, end_node, found):
        if found:
            return found
        print node
        self.set_visited.add(node)
        for adj_value in self.dict_graph[node]:
            if adj_value not in self.set_visited:
                if adj_value not in self.queue:
                    self.dict_parent[adj_value]=node
                    if adj_value == end_node:
                        #print "Found, terminating"
                        return True
                    self.queue.append(adj_value)

        while(self.queue and not found):
            node = self.queue.popleft()
            found = self.bfs_path(node, end_node, found)
            #print "Found while:", found

        return found






def main():
    g_bfs = GraphBFS()
    #g_bfs.bfs('u')
    start_node = 'u'
    end_node = 'w'
    found = g_bfs.bfs_path(start_node, end_node, False)
    if found:
        print "found "
        current_node = end_node
        list_path = []
        while(current_node!=start_node):
            list_path.append(current_node)
            current_node = g_bfs.dict_parent[current_node]
        list_path.append('u')
        print "Path is ", ' '.join(list_path)
    else:
        print "Not found"





main()