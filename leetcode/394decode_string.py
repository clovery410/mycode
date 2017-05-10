class Solution(object):
    def decodeString(self, s):
        stack = []
        s = self.splitString(s)
        for c in s:
            if c == ']':
                cur_string = ''
                while len(stack) > 0:
                    print stack
                    top = stack.pop()
                    if top == '[':
                        break
                    cur_string = top + cur_string
                cur_string = int(stack.pop()) * cur_string
                stack.append(cur_string)
            else:
                stack.append(c)
        return ''.join(stack)

    def splitString(self, s):
        res = []
        start, end = 0, 1
        while end < len(s):
            if s[end] in '[]' or s[end].isdigit() != s[start].isdigit() or s[end].isalpha() != s[start].isalpha():
                res.append(s[start:end])
                start = end
                end = end + 1
            else:
                end += 1
        if end > start: res.append(s[start:end])
        return res

    # second stack solution, without preprocess the string
    def decodeString2(self, s):
        stack = []
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append(num)
                num = 0
            elif c == ']':
                _str = ''
                while stack and type(stack[-1]) is not int and stack[-1].isalpha():
                    _str = stack.pop() + _str
                stack.append(stack.pop() * _str)
            else:
                stack.append(c)
        return ''.join(stack)

    # # recursive solution
    # def decodeString3(self, s):
    #     def dfs(idx):
    #         if idx >= len(s):
    #             return ''
    #         num = 0
    #         str_list = []
    #         for i in xrange(idx, len(s)):
    #             if s[i].isalpha():
    #                 str_list.append(s[i])
    #             elif s[i].isdigit():
    #                 num = num * 10 + int(s[i])
    #             elif s[i] == '[':
    #                 following = dfs(i+1)
    #                 for k in range(num):
    #                     str_list.append(following)
    #             elif s[i] == ']':
    #                 return ''.join(str_list)

    #     return dfs(0)
    
    #parse solution
    def decodeString4(self, s):
        def peekNextToken():
            if self.idx < len(s):
                return s[self.idx]
            return None
        
        def getNextToken():
            # eat all empty spaces
            while self.idx < len(s) and s[self.idx] == ' ':
                self.idx += 1

            if self.idx >= len(s):
                return None
            
            # token is [ or ]
            if s[self.idx] in '[]':
                ret = s[self.idx]
                self.idx += 1
                return ret

            # token is number or string
            else:
                token_sample = s[self.idx]
                ret = ''
                while self.idx < len(s) and s[self.idx].isdigit() == token_sample.isdigit() and s[self.idx].isalpha() == token_sample.isalpha():
                    ret += s[self.idx]
                    self.idx += 1
                return ret
                    
        def eatString():
            res = []
            while True:
                if peekNextToken() is None:
                    break
                if peekNextToken() == ']':
                    getNextToken()
                    break
                num, string = eatPair()
                res.append(num * string)
            return ''.join(res)

        def eatPair():
            num = int(eatNumber())
            getNextToken()
            string = eatChar()
            return num, string

        def eatNumber():
            return getNextToken()

        def eatChar():
            string = getNextToken()
            while peekNextToken() != ']':
                if peekNextToken().isdigit():
                    string += eatString()
                else:
                    string += getNextToken()
            return string

        self.idx = 0
        return eatString()

if __name__ == "__main__":
    sol = Solution()
    print sol.decodeString2("3[a2[c]]")
    print sol.decodeString3("3[a2[c]]")
                    
