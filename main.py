import random, copy, csv

OPTIONS = "1. start the randomizer" \
          "\n2. view the current dictionary" \
          "\n3. edit the dictionary" \
          "\n4. reset the remaining characters" \
          "\n5. exit\n"

PLAYERS_MSG = "PLEASE EDIT THIS FILE USING THE MENU"

def init_cd():
    CD = {}
    i = 1
    fp = open("chars", "r")
    for line in fp:
        line = line.strip()
        CD[i] = line
        i += 1
    fp.close()
    return CD

def init_pd():
    PD = {}
    fp = open('players', 'r')
    fp.readline()
    while True:
        k = fp.readline()
        v = fp.readline()
        if not k or not v:
            break
        PD[k.strip()] = v.strip().split(',')
    fp.close()
    for key in PD:
        for i in range(len(PD[key])):
            PD[key][i] = int(PD[key][i])
    return PD

def init_rd():
    gp = open('remaining.csv', 'r', encoding='utf8')
    reader = csv.reader(gp)
    RD = {}
    for line in reader:
        RD[line[0]] = line[1:]
    gp.close()
    for key in RD:
        for i in range(len(RD[key])):
            RD[key][i] = int(RD[key][i])
    return RD

def write_remaining(RD):
    gp = open('remaining.csv', "w", newline='', encoding='utf8')
    writer = csv.writer(gp)
    ML = []
    for key in RD:
        GL = [key]
        GL.extend(RD[key])
        ML.append(GL)

    for l in ML:
        writer.writerow(l)
    gp.close()

def display_chars(CD):
    i = 1
    while True:
        print("{:2s}".format(str(i)) + ": {:20s}".format(CD[i]), end='')
        i += 1
        if len(CD) > i:
            print("{:2s}".format(str(i)) + ": {:20s}".format(CD[i]), end='')
            i += 1
        else:
            break
        if len(CD) > i:
            print("{:2s}".format(str(i)) + ": {:20s}".format(CD[i]), end='')
            i += 1
        else:
            break
        print()

def update_players(PD):
    fp = open('players', 'w', encoding='utf8')
    fp.write(PLAYERS_MSG + '\n')
    for key in PD:
        fp.write(key + '\n')
        for i in range(len(PD[key])):
            PD[key][i] = str(PD[key][i])
        fp.write(','.join(PD[key]) + '\n')
    fp.close()

def pick_chars(RD, PD, CD):
    for key in PD:
        if not len(RD[key]):
            print("{:>15s}".format(key), "has been reset.")
            RD[key] = copy.deepcopy(PD[key])
        rng = random.choice(RD[key])
        RD[key].remove(rng)
        print("{:>15s} got".format(key), CD[rng])
        write_remaining(RD)

def view_dic(RD, PD, CD):
    i = 1
    temp = {}
    print("players:")
    for key in PD:
        print("{:2s}: {:15s}".format(str(i), key))
        temp[str(i)] = key
        i+=1
    op = input("who u tryna see?\n")
    for j in PD[temp[op]]:
        rem = ""
        if j in RD[temp[op]]:
            rem = "*"
        print("{:2s}{:20s}".format(rem, CD[j]))
    print("\na * means that char is in the remaining dict.\n")

def main():
    ''''''

    CD = init_cd()  # character name dictionary
    PD = init_pd()  # player dictionary (see players.txt)
    RD = init_rd()  # remaining dictionary (see remaining.csv)

    print("Welcome to smash_randomizer\na GoatProvject")
    print("THINGS PLANNED:\n  choose who's playing in the current session\n  (will only choose characters for those keys)🤓"
          "\n  add/remove one character to a key")

    while True:
        op = input(OPTIONS)
        if op == '1':
            while True:
                print('\n')
                pick_chars(RD, PD, CD)
                if input("\nhit enter for new char"
                         "\ntype exit to leave\n") == 'exit':
                    break
        elif op == '2':
            view_dic(RD, PD, CD)
        elif op == '3':
            k = input("input the key you wish to add/edit."
                      "\ninput !D to delete a player\n")
            if k == '!D':
                for key in PD:
                    print(key)
                k2 = input("\nenter the player to delete:\n")
                PD.pop(k2)
                RD.pop(k2)
            else:
                display_chars(CD)
                v = input('\nenter the desired character indexes'
                      '\nformat: "x,x,x,x,x,x,x"\n')
                v = v.split(',')
                for i in range(len(v)):
                    v[i] = int(v[i])
                PD[k] = v
                RD[k] = v
            print(PD)
            update_players(PD)
            write_remaining(RD)
            print("successfully updated. must restart to take effect.")
            break
        elif op == '4':
            for key in RD:
                RD[key] = copy.deepcopy(PD[key])
            write_remaining(RD)
            print("done")
        elif op == '5':
            break
main()