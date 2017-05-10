import random

trj_noise = [5,6,7,8,9,10]
output = []

def generate_fix_pattern():
    fix_pattern = []
    # 80% add 1
    if random.randint(1,5) != 1:
        fix_pattern.append(1)
    # 50%-75% add 2
    if random.randint(1,random.randint(2,4)) != 1:
        fix_pattern.append(2)
    # 50%-75% add 3
    if random.randint(1,random.randint(2,4)) != 1:
        fix_pattern.append(3)
    # 87.5% add 4
    if random.randint(1,8) != 1:
        fix_pattern.append(4)
    return list(fix_pattern)



for i in range(20):
    trj = generate_fix_pattern()
    noise_count = random.randint(1,len(trj_noise))

    for noise in random.sample(trj_noise, noise_count):
        position = random.randint(0,len(trj))
        # 10%-12.5%
        if random.randint(1,random.randint(8,10)) == 1:
            trj.insert(position, noise)

    print(trj)
    output.append(trj)

# print (output)



