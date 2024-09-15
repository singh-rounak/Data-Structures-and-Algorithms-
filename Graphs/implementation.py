class Graph:
    def __init__(self, edges):
        self.edge = edges
        self.graph_dict = {}

        for start, end in edges:   
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print("Routes are: ", self.graph_dict)
             
    #recursive function with a variable to store state
    def get_paths(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return [path]
            
        if start not in self.graph_dict:
            return []
        
        
        paths =[]
        #value is value from {"key":"value"}
        for value in self.graph_dict[start]:
            if value not in path:
                new_paths = self.get_paths(value, end,path)
                for i in new_paths:
                    paths.append(i)
        return paths
    
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path
    

#=================
if __name__ == '__main__':
    #This is a list of Tuples and each tuple has (start, end)
    routes = [
    ("Mumbai","Pune"),
    ("Mumbai", "Surat"),
    ("Surat", "Bangaluru"),
    ("Pune","Hyderabad"),
    ("Pune","Mysuru"),
    ("Hyderabad","Bangaluru"),
    ("Hyderabad", "Chennai"),
    ("Mysuru", "Bangaluru"),
    ("Chennai", "Bangaluru")
]

    my_routes  = Graph(routes)
    my_routes

    start = "Mumbai"
    end = 'Bangaluru'
    print(f"All paths between {start} and {end} are:",my_routes.get_paths(start, end))
    print(f"Shortest paths between {start} and {end} are:",my_routes.get_shortest_path(start, end))

