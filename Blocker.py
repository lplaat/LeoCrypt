import random
import json

def gen_map(seed, max):
    random.seed(seed)
    map = []
    for y in range(max[1]):
        map.append([])
        for _ in range(max[0]):
            map[y].append(random.randint(0, 1114111))

    return map

def step(i, seed, step_map, max):
    steps_map = json.loads(json.dumps(step_map))
    go = True
    while go:
        random.seed(seed)

        for _ in range(len(steps_map)):
            t_x = random.randint(0, max[0]-1)
            t_y = random.randint(0,  max[1]-1)

        t_out = [random.randint(0,  max[0]-1), random.randint(0, max[1]-1)]

        found = False
        for stemp in steps_map:
            if json.dumps(stemp) == json.dumps(t_out):
                found = True
                steps_map.append([None, None])
        
        if found == False:
            go = False
            steps_map.append(t_out)
            return [t_out, steps_map]


def incrypt_part(a, b, seed):
    return a + b

def decrypt_part(a, b, seed):
    if a == 690 or a == 420:
        return None
    return a - b

def incrypt_block(input, max):
    input = [ord(character) for character in input]

    if not (max[0] * max[1]) < len(input)+2:
        seed = random.randint(10**15, 10**16)
        map = gen_map(seed, max)

        input.append(690)
        input.append(420)

        jumps = 0
        sec = []
        for part in input:
            point = step(jumps, seed, sec, max)
            sec = point[1]
            map[point[0][1]][point[0][0]] = incrypt_part(part, map[point[0][1]][point[0][0]], seed)
            jumps += 1

        map_out = []
        for y in range(max[1]):
            map_out.append([])
            for x in range(max[0]):
                map_out[y].append(chr(map[y][x]))

        return [seed, map_out]
    else:
        return 'To large to put in block!'

def decrypt_block(input):
    seed = input[0]
    input = input[1]
    clean_map = gen_map(seed, [len(input[0]), len(input)])
    map = []

    for y in range(len(input)):
        map.append([])
        for x in range(len(input[0])):
            map[y].append(ord(input[y][x]))

    string = []
    jumps = 0
    sec = []
    go = True
    past = None
    while go:
        point = step(jumps, seed, sec, [len(input[0]), len(input)])
        sec = point[1]
        jumps += 1

        out_part = decrypt_part(map[point[0][1]][point[0][0]], clean_map[point[0][1]][point[0][0]], seed)
        if not out_part == None:
            string.append(out_part)

        if past == 690 and decrypt_part(map[point[0][1]][point[0][0]], clean_map[point[0][1]][point[0][0]], seed) == 420:
            go = False

        past = decrypt_part(map[point[0][1]][point[0][0]], clean_map[point[0][1]][point[0][0]], seed)
        if jumps > (len(input)*len(input[0]))-1:
            print('No stopping code found')
            go = False

    out_string = ''
    for part in string:
        out_string += chr(part)

    return out_string
