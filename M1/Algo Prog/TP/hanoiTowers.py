# departure tower
# destination tower
# third tower that is neither
#%%
towerlst = [[2],[3],[1]]

def thirdTower(dep, dest):
    if (dep == 0 and dest == 1) or (dep == 1 and dest==0):
        return 2
    elif (dep == 0 and dest == 2) or (dep == 2 and dest == 0):
        return 1
    else:
        return 0

def displaysMovement(dep, dest):
    return print("T" + str(dep) + " --> T" + str(dest))

def motion(towerlst, dep, dest, nb_disques = 0):
    print(towerlst)
    towerlst[dest] = towerlst[dep][0:nb_disques] + towerlst[dest]
    towerlst[dep] = towerlst[dep][nb_disques:]
    displaysMovement(dep, dest)
    print(towerlst)
    return towerlst

def movementIsValid(towerlst, dep, dest):
    # returns True if and only if deb and dest belong to {0,1,2}
    # all one statement?
    return ((dep in [0, 1, 2] and dest in [0, 1, 2]) and (dep != dest) and (towerlst[dep] != []) and (towerlst[dest] == [] or (towerlst[dep][0] < towerlst[dest][0])))


    # dep and dest are different

    # the starting tower is not empty
    # the first disc of the starting tower is smaller 
    # than the first disc of the destination tower
towerLst = [[1,2,3],[],[]]

def movementMultiDisk(towerlst, dep, dest, nb_disques):
    # checks movement from dep to dest is indeed valid: call isValid
    # if nb_disques == 0; return towerlst
    # if yes: move the upper disks of dep to dest: call move


    if nb_disques == 0:
        return towerlst
    elif movementIsValid(towerlst, dep, dest) == True:

        return motion(towerlst, dep, dest, nb_disques) #movementMultiDisk(motion(towerlst, dep, dest, nb_disques), dep, dest, nb_disques-1)
    else:
        displaysMovement(dep, dest)
        print(towerlst)
        return towerlst

print(movementIsValid(towerlst, 2, 0))

movementMultiDisk(towerLst, 0, 2, 1)

# %%
