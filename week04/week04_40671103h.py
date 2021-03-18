

def file_read(file_loc):
    with open(file_loc, encoding="utf-8") as f:
        text = f.read()
    return text


if __name__== "__main__":
    
    topic1 = file_read("./example/DogPeople.txt")
    
    dbp=[]
    dbp.append(("婦人",topic1.count('婦人')))
    dbp.append(("土狗",topic1.count('土狗')))
    dbp.append(("男",topic1.count('男')))
    
    topic2 = file_read("./example/PeopleDog.txt")

    pbd=[]
    pbd.append(("婦人",topic1.count('婦人')))
    pbd.append(("土狗",topic1.count('土狗')))
    pbd.append(("男",topic1.count('男')))

    print('dbp: ',dbp)
    print('pbd: ',pbd)