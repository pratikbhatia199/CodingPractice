__author__ = 'pratik'

class DFS:
    set_visited = set()
    set_visiting = set()
    dict_graph = {'u':['v','x'],
                  'v':['y'],
                  'w':['z','y'],
                  'x':['v'],
                  'y':['x'],
                  'z':['z']
                  }


    def dfs(self, node):
        if node in self.set_visited:
            return
        if node in self.set_visiting:
            return
        else:
            self.set_visiting.add(node)
            for adj_node in self.dict_graph[node]:
                self.dfs(adj_node)
        print node
        self.set_visited.add(node)

def main():
    dfs_search = DFS()
    dfs_search.dfs('u')

    set_not_connected = set(dfs_search.dict_graph.keys())-dfs_search.set_visited
    while(set_not_connected):
        for node in set_not_connected:
            dfs_search.dfs(node)
            set_not_connected=set(dfs_search.dict_graph.keys())-dfs_search.set_visited


main()



