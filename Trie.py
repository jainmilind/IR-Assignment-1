class Trie : 
    def __init__(self) : 
        self.child = dict()
        self.end = False
        self.cnt = 0
        
    def insert(self , word) : 
        root = self
        for char in word :
            if root.child.get(char) == None :
                root.child[char] = Trie()
            root = root.child[char]
        root.cnt += 1
        root.end = True
    
    def wildcard(self , word) : 
        ans , cur = set() , word
        root = self
        for char in word : 
            if root.child.get(char) == None : 
                return ans
            root = root.child[char]
        def dfs(node , cur) :
            if node.end == True : 
                ans.add(cur)
            for label in node.child : 
                newstr = cur + label
                dfs(node.child[label] , newstr)
        dfs(root , word)
        return ans