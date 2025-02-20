import random

def uname_gen(full_name:list, format:str="First:F::1,Second:S:opt:2,Third::3,Fourth:F:opt:4", canrepeat:bool=False):
    positions = format.split(',')
    for pos in positions:
        param = pos.split(':')
        if param[1] != "":
            print(param)
            print(param[1], param[0])
            param_index = param[0].find(param[1])
            print(param_index)
            print(full_name[0][param_index], full_name[0], param[1], param[0])
        else:
            print(param)

    for name in full_name:
        print(name)


if __name__ == '__main__':
    uname_gen(full_name=["Felix", "Delgadillo", "Barrios"])