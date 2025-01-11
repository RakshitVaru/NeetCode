class Graph:
    
    def __init__(self):
        self.adj_list={}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src]=[]
        if dst not in self.adj_list:
            self.adj_list[dst]=[]
        self.adj_list[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        return self.dfs(src,dst,set())

    def dfs(self, src, dst, visit):
        if src==dst:
            return True
        
        # visit.add(src)
        for neighbour in self.adj_list[src]:
            # print(src, neighbour)    
            if neighbour not in visit:
                if self.dfs(neighbour, dst, visit):
                    return True
        return False
