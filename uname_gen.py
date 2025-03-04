import random

class NameIsTooShort(Exception):
    def __init__(self,msg=None):
        self.msg = msg
        print("Error: Name is too short")

def uname_gen(name:str, format:str="First:F::1,Second:S:opt:2,Third:::3,Fourth:F:opt:4", name_separator:str=" ") -> str:
    uname = ""
    full_name = name.split(name_separator)
    if len(full_name) > 2:
        uname = f"{full_name[0][0]}{full_name[-2]}"
    elif len(full_name) == 2:
        uname = f"{full_name[0][0]}{full_name[-1]}"
    else:
        raise NameIsTooShort(f"{full_name} must have 2 or more names")
    return uname

def uname_list_gen(full_names:list, canrepeat:bool=False, format:str="First:F::1,Second:S:opt:2,Third:::3,Fourth:F:opt:4", name_separator:str=" "):
    unames = []
    for i,name in enumerate(full_names):
        full_name = name.split(name_separator)
        if len(full_name) > 2:
            uname = f"{full_name[0][0]}{full_name[-2]}"
        elif len(full_name) == 2:
            uname = f"{full_name[0][0]}{full_name[-1]}"
        else:
            return {"Error":f"The Name {name} in position {i} is too short","names":unames}
        
        if not canrepeat and uname in unames:
            while uname in unames:
                it = 0 if len(full_name) > 2 else 1
                try:
                    uname += f"{full_name[-1][it]}".upper()
                except Exception as e:
                    return {"Error":f"The user for {name} in position {i} cannot be guessed","names":unames}
                it+=1
            unames.append(uname)
        else:
            unames.append(uname)
    return unames

if __name__ == '__main__':
    un = uname_list_gen(full_names=["Jose Eleuterio Gomez Morin", "Sebastin Lerdo Tejada", "Jorge Gomez"])
    print(un)