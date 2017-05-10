class TreeNode(object):
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.supervisor = None
        self.subordinate = list()
        
class Solution(object):
    def partyInvitation(self, relation):
        def dfs(node):
            if not node.subordinate:
                return (node.level, 0)
            
            cur_include, cur_exclude = node.level, 0
            for sub_node in node.subordinate:
                sub_include, sub_exclude = dfs(sub_node)
                cur_include += sub_exclude
                cur_exclude += max(sub_include, sub_exclude)

            return (cur_include, cur_exclude)

        # build Tree
        party_member = {}
        for pair1, pair2 in relation:
            name1, level1 = pair1
            name2, level2 = pair2
            if pair1 not in party_member:
                party_member[pair1] = TreeNode(name1, level1)
            if pair2 not in party_member:
                party_member[pair2] = TreeNode(name2, level2)
            party_member[pair1].subordinate.append(party_member[pair2])
            party_member[pair2].supervisor = party_member[pair1]

        # get Tree root
        for member_node in party_member.values():
            if member_node.supervisor == None:
                root = member_node
                break

        root_include, root_exclude = dfs(root)
        return max(root_include, root_exclude)
        
if __name__ == "__main__":
    sol = Solution()
    relations = [[("1", 10), ("2", 9)], [("1", 10), ("3", 6)], [("2", 9), ("4", 8)], [("4", 8), ("5", 7)], [("1", 10), ("6", 3)]]
    print sol.partyInvitation(relations)
