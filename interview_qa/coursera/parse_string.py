#First, convert a nested dictionary to a string
def convertToString(dictionary):
    def convertHelper(d):
        res = ['{']
        count = 0
        for key, val in d.items():
            res.append(key)
            res.append(":")
            if type(val) == str:
                res.append(val)
            else:
                res.extend(convertHelper(val))
            if count < len(d) - 1:
                res.append(",")
            count += 1
        return res + ["}"]

    strLst = convertHelper(dictionary)
    return ''.join(strLst)

#Second, then parse the string back into a nested dictionary
def convertToDict(string):
    def split(string):
        res = []
        idx = 0
        pre = ''
        for cur in string:
            if cur in '{}:,':
                if pre:
                    res.append(pre)
                    pre = ''
                res.append(cur)
            else:
                pre += cur
        return res
    
    def convert(lst):
        root = {}
        stack = [root]
        is_key = True
        pre_key = None
        for cur in lst[1:]:
            if cur == ':':
                is_key = False
            elif cur == ',':
                is_key = True
            elif cur == '{':
                child = {}
                stack[-1][pre_key] = child
                stack.append(child)
                is_key = True
            elif cur == '}':
                stack.pop()
            elif is_key:
                pre_key = cur
            else:
                stack[-1][pre_key] = cur
        return root
    return convert(split(string))

idx = 0
def parseDictStr(dict_str):
    def getNextToken():
        global idx
        while idx < len(dict_str) and dict_str[idx] == ' ':
            idx = idx + 1
        if idx >= len(dict_str):
            return None
        if not dict_str[idx].isalpha():
            ret = dict_str[idx]
            idx += 1
            return ret
        else:
            word = dict_str[idx]
            idx += 1
            while idx < len(dict_str) and dict_str[idx].isalpha():
                word += dict_str[idx]
                idx += 1
            return word
        
    def peekNextToken():
        global idx
        if idx < len(dict_str):
            return dict_str[idx]
        else: return None

    def eatDict():
        result = {}
        getNextToken()
        while True:
            if peekNextToken() is None:
                break
            if peekNextToken() == '}':
                getNextToken()
                break
            key, val = eatPair()
            result[key] = val
            if peekNextToken() != '}':
                getNextToken()    # eat comma
        return result

    def eatPair():
        key = eatKey()
        val = eatValue()
        return key, val
            
    def eatKey():
        # eat ("'")
        key = getNextToken()
        # eat ("'")
        getNextToken()
        return key

    def eatValue():
        val = peekNextToken()
        if val == '{':
            return eatDict()
        elif val.isalpha:
            return getNextToken()

    return eatDict()


# Program := Statement
# Program := Program + Statement

# Statement :=
#    Assignment
#    While

# While := while conidition + Program

# condition: left_op op right_op

# left_op: expression

# expression: 

    


        
if __name__ == "__main__":
    d = {'a': 'apple', 'b': {'bc': 'banana', 'bd': 'bacon'}, 'c': 'cranberry', 'd': {'da':'dad', 'db': 'database'}}
    s = convertToString(d)
    print convertToDict(s)
    print parseDictStr(s)
