class Solution(object):
    def simplifyPath(self, path):
        path_array = path.split("/")
        stack = []
        for name in path_array:
            if name == "." or name == "":
                continue
            if name == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(name)
                
        return "/" + "/".join(stack)

if __name__ == "__main__":
    sol = Solution()
    path = "//home/foo"
    print sol.simplifyPath(path)
        
