import statistics as s

#while True:
list1 = input("list : ")
list2 = []
list1 = list1.split(";")

for x in list1:
    x = x.replace('$', '')
    x = x.replace('\qquad', '')
    if "l" in x:
        x1 = x.split("l")
        x2 = x1[0]
        x3 = []
        x1 = int(x1[1]) * str(x1[0])
        #print(x1)
        #print(x2)
        for y in x1:
            if y == x2:
                x3.append(str(x2))
                print(x3)
        for z in x3:
            list2.append(float(z))
            #print(list2)
            #print(s.mean(list2))
    else:
        list2.append(float(x))
    list2.sort()
    #print(list2)


def moyenne(nb_point_virgule):
    return s.mean(nb_point_virgule)


def etendue(listnb):
    etendue = max(listnb) - min(listnb)
    return etendue

def mediane(list3):
    length = len(list3)
    if length == 1:
        return None
    elif length % 2 == 0:
        med = moyenne(list((list3[int(length/2)], list3[int(length/2-1)])))
        return med
    elif length % 2 == 1:
        med = list3[int(length/2)]
        return med


print("etendue : {}".format(etendue(list2)))
print("moyenne : {}".format(moyenne(list2)))
print("mediane : {}".format(mediane(list2)))