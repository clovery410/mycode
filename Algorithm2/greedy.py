import operator

def sort_by_difference(lines):
    jobs = list()
    cost = list()
    
    for line in lines[1:]:
        weight = int(line.split()[0])
        length = int(line.split()[1])
        jobs.append([weight, length, weight - length])
        
    jobs = sorted(jobs, key = operator.itemgetter(2, 0), reverse = True)
    return jobs

def sort_by_ratio(lines):
    jobs = list()
    cost = list()
    
    for line in lines[1:]:
        weight = int(line.split()[0])
        length = int(line.split()[1])
        jobs.append([weight, length, weight * 1.0 / length])
        
    jobs = sorted(jobs, key = operator.itemgetter(2), reverse = True)
    return jobs

def calculate(jobs, num):
    cost = [0 for x in range(num)]
    cost[0] = jobs[0][1]
    
    for i in range(1, num):
        cost[i] = cost[i - 1] + jobs[i][1]
    total_cost = 0
    for i in range(num):
        total_cost += (cost[i] * jobs[i][0])
    return total_cost
    
f = open('jobs.txt')
content = f.read()
lines = content.splitlines()
num = int(lines[0])

jobs = sort_by_difference(lines)
new_jobs = sort_by_ratio(lines)

result1 = calculate(jobs, num)
result2 = calculate(new_jobs, num)
print(result1)
print(result2)
