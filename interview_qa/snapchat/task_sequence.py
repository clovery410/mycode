import collections
class Task(object):
    def __init__(self, _id):
        self._id = _id
        self.deps = set()
        
class Solution(object):
    def taskSequence(self, tasks):
        in_degree = collections.defaultdict(list)
        out_degree = collections.defaultdict(int)

        # build graph
        for task in tasks:
            for parent_task in task.deps:
                in_degree[parent_task].append(task)
                out_degree[task] += 1

        # do topological sort
        order = []
        sinks = []
        for task in tasks:
            if task not in out_degree:
                sinks.append(task)

        while sinks:
            cur_task = sinks.pop()
            order.append(cur_task._id)
            for parent_task in in_degree[cur_task]:
                out_degree[parent_task] -= 1
                if out_degree[parent_task] == 0:
                    sinks.append(parent_task)

        # detect cycle
        if len(order) < len(tasks):
            print "There is Cycle"
            return None
        
        return order

if __name__ == "__main__":
    task1 = Task(1)
    task2 = Task(2)
    task3 = Task(3)
    task4 = Task(4)
    task5 = Task(5)

    task2.deps.add(task1)
    task2.deps.add(task3)
    task3.deps.add(task5)
    task4.deps.add(task1)
    task4.deps.add(task2)
    # task4.deps.add(task5)
    task5.deps.add(task4)
    
    tasks = [task1, task2, task3, task4, task5]

    sol = Solution()
    print sol.taskSequence(tasks)
    
    
    
