from helpers import *

odata = [int(x) for x in get_input(2)[0].split(",")]

# Part 1
def run(data, pc):
    while True:
        opcode = data[pc]
        if opcode == 99:
            break
        op1, op2, dst = data[pc+1:pc+4]
        if opcode == 1:
            data[dst] = data[op1] + data[op2]
            pc += 4
            continue
        elif opcode == 2:
            data[dst] = data[op1] * data[op2]
            pc += 4
            continue
        else:
            return -1
    return data[0]

def restore(odata):
    data = [d for d in odata]
    data[1] = 12
    data[2] = 2
    return run(data, 0)

print(restore(odata))

# Part 2

def find_nv(data):
    found = False
    for noun in range(100):
        for verb in range(100):
            #print(noun, verb)
            mod = [d for d in odata]
            mod[1] = noun
            mod[2] = verb
            res = run(mod, 0)
            if res == 19690720:
                return 100*noun+verb
    return None

print(find_nv(odata))


