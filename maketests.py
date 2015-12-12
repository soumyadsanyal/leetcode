import random

def make_random_list_suite(population, numbercases, filename):
    l=[random.randint(0,len(population)) for index in range(numbercases)]
    print(l)
    make_list(population,l[0],filename,overwrite=True)
    for term in l[1:]:
        make_list(population,term,filename,overwrite=False)
    

def make_list(population, length, filename, otherlines=2, overwrite=False):
    if length==0:
        result=[]
    result=random.sample(population, length)
    if overwrite==False:
        option="a"
    else:
        option="w"
    with open(filename,option) as f:
        if result==[]:
            f.write("[]\n")
            for term in range(otherlines):
                f.write("%s\n"%0)
            return 1
        f.write("[")
        for index in range(max(0,len(result)-2)):
            f.write("%d,"%result[index])
        f.write("%d]\n"%result[-1])
        top=0
        for term in range(otherlines):
            a=random.randint(top,len(result)-1)
            f.write("%s\n"%random.randint(top,len(result)-1))
            top=a
    return 1


