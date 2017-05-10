class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(word, start_i, curr_solution, all_solutions):
            if start_i >= len(word):
                all_solutions.append(''.join(curr_solution))
            else:
                curr_solution.append(word[start_i])
                helper(word, start_i + 1, curr_solution, all_solutions)
                curr_solution.pop()
                count = 0
                for i in xrange(len(word) - start_i):
                    count += 1
                    curr_solution.append(str(count))
                    if start_i + count < len(word):
                        curr_solution.append(word[start_i + count])
                        helper(word, start_i + count + 1, curr_solution, all_solutions)
                        curr_solution.pop()
                    else:
                        helper(word, start_i + count, curr_solution, all_solutions)
                    curr_solution.pop()
                    
        all_solutions = []
        helper(word, 0, [], all_solutions)
        
        return all_solutions
