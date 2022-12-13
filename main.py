import random, copy, csv

def write_goated(VD):
    gp = open('goated.csv', "w", newline='', encoding='utf8')
    writer = csv.writer(gp)
    ML = []
    for key in VD:
        GL = [key]
        GL.extend(VD[key])
        ML.append(GL)

    for l in ML:
        writer.writerow(l)
    gp.close()

def read_goated():
    gp = open('goated.csv', 'r', encoding='utf8')
    reader = csv.reader(gp)

    VD = {}
    for line in reader:
        VD[line[0]] = line[1:]
    gp.close()
    return VD

CD = {}
i = 1
fp = open("chars", "r")
for line in fp:
    line = line.strip()
    CD[i] = line
    i+=1
#print(CD)

'''
player dictionary. handles all possible character selections
'''
PD = {}
PD["ant cap"] = [1,2,3,4,5,6,8,9,12,13,15,16,17,18,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,44,45,46,47,48,49,54,55,56,58,59,62,63,66,68,70,72,73,74,75,76,79,80,82,83]
PD["sid"] = [1,2,3,4,5,9,10,11,12,14,15,16,19,20,23,24,25,26,27,28,29,35,37,38,39,45,46,47,62,66,69,74,76,80,83,84,86]
PD["s_dada"] = [1,2,3,4,5,7,9,10,11,12,13,14,16,17,18,20,21,23,24,25,26,27,28,29,30,33,34,35,37,38,39,42,45,46,47,52,62,71,72,73,74,75,76,77,79,80,82,83,84,85]
#PD["gay"] = [1]
#PD["test"] = [1,2,3]
gunner = ["Rock Lee", "Toad", "TRACK STAR", "IGotHoooes"]

'''
visited dictionary, initally same as PD but removes the element after drawn
'''

#VD = read_goated()
#print("vd:", VD)

VD = {}
for key in PD:
    VD[key] = copy.deepcopy(PD[key])

while True:
    for key in PD:
        if not len(VD[key]):
            VD[key] = copy.deepcopy(PD[key])
        rng = random.choice(VD[key])
        VD[key].remove(rng)
        print(key, "got", CD[rng])
    ask = input("hit enter for new char")
    print("\n" * 50)
    if ask:
        break

write_goated(VD)
