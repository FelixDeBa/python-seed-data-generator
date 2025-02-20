import json, random

def name_gen(sex:str="both", canrepeat:bool=True, country:str="mexico", quantity:int=1):
    full_names=[]
    
    with open('data/nombres.json', 'r') as file:
        names = json.load(file)
    i=1
    if sex.lower() == "both":
        while i <= quantity:
            sex=random.choice(list(names[country]["first_name"].keys()))
            first_names = [random.choice(names[country]["first_name"][sex]) for j in range(random.randrange(1,3))]
            last_names = [random.choice(names[country]["last_name"]) for k in range(2)]

            if not canrepeat and { 'name': ' '.join(first_names), 'last_name':' '.join(last_names), 'sex':sex } in full_names:
                i-=1
            else:
                full_names.append({ 'name': ' '.join(first_names), 'last_name':' '.join(last_names), 'sex':sex })
                i+=1
    elif sex.lower() in ["male", "female", "f", "m"]:
        while i <= quantity:
            first_names = [random.choice(names[country]["first_name"][sex]) for j in range(random.randrange(1,3))]
            
            last_names = [random.choice(names[country]["last_name"]) for k in range(2)]
            
            if not canrepeat and { 'name': ' '.join(first_names), 'last_name':' '.join(last_names), 'sex':sex } in full_names:
                i-1
            else:
                full_names.append({ 'name': ' '.join(first_names), 'last_name':' '.join(last_names), 'sex':sex })
                i+=1
    else:
        return {"message":"Error please select sex as male, female or both"}
    return full_names

if __name__ =='__main__':
    qty = random.randint(1,10)
    personas = name_gen(quantity=qty, sex="male")
    for persona in personas:
        print(f'{persona["name"]} {persona["last_name"]}')