import json, random

def name_gen(sex:str="both", repeat:bool=True, country:str="mexico", quantity:int=10):
    full_names=[]
    
    with open('data/nombres.json', 'r') as file:
        names = json.load(file)

    if sex.lower() == "both":
        for i in range(quantity):
            sex=random.choice(list(names[country]["first_name"].keys()))
            first_names = [random.choice(names[country]["first_name"][sex]) for j in range(random.randrange(1,3))]
            
            last_names = [random.choice(names[country]["last_name"]) for k in range(2)]
            full_names.append({ 'name': ' '.join(first_names), 'last_name':' '.join(last_names), 'sex':sex })
    elif sex.lower() in ["male", "female", "f", "m"]:
        for i in range(quantity):
            first_names = [random.choice(names[country]["first_name"][sex]) for j in range(random.randrange(1,3))]
            
            last_names = [random.choice(names[country]["last_name"]) for k in range(2)]
            full_names.append({ 'name': ' '.join(first_names), 'last_name':' '.join(last_names), 'sex':sex })
    else:
        return {"message":"Error please select sex as male, female or both"}
    return full_names

personas = name_gen(quantity=10, sex="male")
for persona in personas:
    print(f'{persona["name"]} {persona["last_name"]}')