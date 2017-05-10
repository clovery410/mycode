class Solution(object):
    def __init__(self):
        self.log_file = open('banker_log.txt', 'w')

    def print_log(self, msg):
        print msg
        self.log_file.write(msg + '\n')

    def banker_algo(self, max_amount, curr_allocate, available_r, finish_process):
        if len(finish_process) == len(max_amount):
            self.print_log("All Processes are done!")
            return
        
        row, col = len(max_amount) - len(finish_process), len(max_amount[0])
        still_need = [[0 for x in xrange(col)] for x in xrange(row)]

        # Compute the resourses each processes still needs
        remaining_process = []
        for i in xrange(len(max_amount)):
            if i in finish_process:
                continue
            else:
                remaining_process.append(i)
                curr_idx = len(remaining_process) - 1
                for j in xrange(col):
                    still_need[curr_idx][j] = max_amount[i][j] - curr_allocate[i][j]

        # Check whether there exists any processes whose requests can be satisfied, adding those satisfiable processes into satisfied_process list
        satisfied_process = []
        for i in xrange(len(remaining_process)):
            process = remaining_process[i]
            satisfy = True
            for j in xrange(col):
                satisfy &= still_need[i][j] <= available_r[j]
            if satisfy:
                satisfied_process.append(process)
                self.print_log("The request for Process %d can be fulfilled by the current available resources, it asks for %s in total, already allocated %s, still needs %s, and system available is %s" % (process, max_amount[process], curr_allocate[process], still_need[i], available_r))
            else:
                self.print_log("Process %d cannnot be fulfilled at this run, it asks for %s in total, alreay allocated %s, still needs %s, and system available is %s" % (process, max_amount[process], curr_allocate[process], still_need[i], available_r))

        # After checking each process's request, determine whether there is a deadlock!
        if len(satisfied_process) == 0:
            self.print_log("No more processes can be scheduled any more, deadlocked!")
            return

        # If no deadlock currently, just pick the first process in the satisfied_process list to run to completion
        chosen = satisfied_process[0]
        finish_process.append(chosen)

        # Adding the previously allocated resources of that process back to system available
        for j in xrange(col):
            available_r[j] += curr_allocate[chosen][j]
        self.print_log("Pick process %d to run, upon its finishing, system available resources becomes %s" % (chosen, available_r))

        # Go to next round
        return self.banker_algo(max_amount, curr_allocate, available_r, finish_process)


if __name__ == '__main__':
    sol = Solution()
    max_amount = [[1,1,2,1,3], [2,2,2,1,0], [2,1,3,1,0], [1,1,2,2,1]]
    allocated = [[1,0,2,1,1], [2,0,1,1,0], [1,1,0,1,0], [1,1,1,1,0]]
    available = [0,0,2,1,1]
    sol.banker_algo(max_amount, allocated, available, [])
