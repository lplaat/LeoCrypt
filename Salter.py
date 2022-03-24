import random

def incrypt(msg):
    Salt = random.randint(10**15, 10**16)
    msg_list = []
    msg_salte = []

    abc = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5','6','7', '8', '9']

    for part in msg:
        for letter_id in range(len(abc)):
            if part.lower() == abc[letter_id].lower():
                msg_list.append(letter_id)

    part_seed = Salt
    for i in msg_list:
        random.seed(part_seed)
        part_seed = random.randint(10**15, 10**16)
        random.seed(part_seed)
        msg_salte.append(i+random.randint(0, 20))
    return [Salt, msg_salte]

def decrypt(Salt, msg):
    try:
        abc = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5','6','7', '8', '9']
        decrypt_msg_array = []
        part_seed = Salt
        msg_string = ""

        for i in msg:
            random.seed(part_seed)
            part_seed = random.randint(10**15, 10**16)
            random.seed(part_seed)
            decrypt_msg_array.append(i - random.randint(0, 20))

        for part in decrypt_msg_array:
            for letter_id in range(len(abc)):
                if part == letter_id:
                    msg_string += abc[letter_id].lower()
        return msg_string
    except:
        return "Decrypter faild"
