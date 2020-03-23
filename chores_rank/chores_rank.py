import random as rd


#initial

pref_by_person = [[1, 2, 3, 4], [1,2,3, 4], [2,4,1,3]]
person = [[] for i in range(len(pref_by_person))]
assigned = []

def by_chores(x,pref_by_person):
    by_chores = []
    for i in range(x):
        by_chores.append([person[i] for person in pref_by_person])
    return by_chores

def has(pref, by_chores):
    has_one = []
    for chore in by_chores:
        temp = []
        for idx, val in enumerate(chore):
            if val == pref:
                temp.append(idx)
        has_one.append(temp)
    return has_one


def random_assign(indices_of):
    assigned = []
    for h in indices_of:
        if h:
            assigned.append(rd.sample(h,1)[0])
        else:
            assigned.append(-1)
    return assigned

def assign_chores(person, assigned):
    for idx, val in enumerate(assigned):
        if val != -1:
            person[idx].append(val)
    return person


def remove_chores(by_chores, assigned):
    for idx, val in enumerate(assigned):
        if val != -1:
            by_chores.pop(idx)
            by_chores.insert(idx,None)
    return by_chores

by_chores = by_chores(4,pref_by_person)

indices_of = has(1,by_chores)

assigned = random_assign(indices_of)

person = assign_chores(person, assigned)

by_chores = remove_chores(by_chores, assigned)
print(by_chores)
print(person)

if __name__ == "__main__":
    pass

