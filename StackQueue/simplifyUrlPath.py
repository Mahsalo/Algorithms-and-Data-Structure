### simplify url path: remove  single dots and slashes and only use stack to keep track of the double dots which cause the current element to drop. 

class Solution:
    def simplifyPath(self, path: str) -> str:
        path_l = path.split("/")
        path_l = [item for item in path_l if item != ""]
        path_l = [item for item in path_l if item != "."]


        print(path_l)
        stck = []
        for i in path_l:
            if i == "..":
                if stck:
                    stck.pop() 
              
            else:
                stck.append(i)
            
               
         
     
        new_path = "/"+"/".join(stck)
        print(new_path)
        return new_path

