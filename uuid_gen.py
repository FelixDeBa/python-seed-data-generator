import random

def uuid_gen(uuid_format:str="8-4-4-4-12") -> str:
    lang_seed = [chr(a) for a in range(48, 58)] + [chr(b) for b in range(97,123)]
    nums = [int(n) for n in uuid_format.split('-')]
    uuid = ""

    for num in nums:
        [uuid:=uuid+lang_seed[random.randrange(0,len(lang_seed)-1)] for place in range(num)]
        uuid+="-"

    return uuid[:-1]


def uuid_list_gen(uuid_format:str="8-4-4-4-12", repeat:bool=False, quantity:int=1) -> list:
    uuid_list = []
    if(repeat):
        uuid_list = [(uuid_gen(uuid_format=uuid_format)) for iter in range(quantity)]
    else:
        for iter in range(quantity):
            if (uuid := uuid_gen(uuid_format=uuid_format)) not in uuid_list:
                uuid_list.append(uuid)
            else:
                iter-=1
    return uuid_list

print(uuid_list_gen(repeat=False, quantity=2))
