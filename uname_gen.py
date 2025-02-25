import random

def uname_gen(name:str, format:str="First:F::1,Second:S:opt:2,Third:::3,Fourth:F:opt:4", name_separator:str=" ") -> str:
    uname = ""
    full_name = name.split(name_separator)
    positions = format.split(',')
    print(positions)
    for i, pos in enumerate(positions):
        parameters = pos.split(':')
        if parameters[2] != "opt":
            if parameters[1] != "":
                index = parameters[0].find(parameters[1])
                uname+=f"{full_name[int(parameters[3])][index]}"
            else:
                uname+=f"{full_name[int(parameters[3])]}"
    return uname

def uname_list_gen(full_names:list, quantity:int, canrepeat:bool=False, format:str="First:F::1,Second:S:opt:2,Third:::3,Fourth:F:opt:4", name_separator:str=" "):
    for full_name in full_names:
        print(full_name.split(name_separator))

if __name__ == '__main__':
    un = uname_gen(name="Jose Eleuterio Gomez Morin")
    print(un)