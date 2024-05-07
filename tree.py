import numpy as np

def get_turn(m):
    ones=0
    for i in range(0,3):
        for j in range(0,3):
            if m[i][j]==1 or m[i][j] ==-1:
                ones+=1
    return ones
def possible_states(m):
    treedic=dict()
    value=0
    t=get_turn(m)
    if evaluate(m)==0:
        if t%2==0:
            for i in range(0,3):
                for j in range(0,3):
                    if m[i][j]==0:
                        tem=np.array(m)
                        tem[i][j]+=1
                        treedic[value]=tem
                        value+=1

        if t%2==1:
            for i in range(0,3):
                for j in range(0,3):
                    if m[i][j]==0:
                        tem=np.array(m)
                        tem[i][j]-=1
                        treedic[value] = tem
                        value += 1
    return treedic
def evaluate(mou):
    t = get_turn(mou)
    if mou[0][0] == mou[1][1] == mou[2][2] == 1 or mou[0][0] == mou[1][1] == mou[2][2] == -1:
        if t%2==1:
            return 1.0
        else:
            return -1.0
    if mou[0][2] == mou[1][1] == mou[2][0] == 1 or mou[0][2] == mou[1][1] == mou[2][0] == -1:
        if t%2==1:
            return 1.0
        else:
            return -1.0
    for i in range(0, 3):
        if mou[i][0] == mou[i][1] == mou[i][2] == 1 or mou[i][0] == mou[i][1] == mou[i][2] == -1:
            if t % 2 == 1:
                return 1.0
            else:
                return -1.0
        if mou[0][i] == mou[1][i] == mou[2][i] == 1 or mou[0][i] == mou[1][i] == mou[2][i] == -1:
            if t % 2 == 1:
                return 1.0
            else:
                return -1.0
    return 0
class tree():
    def __init__(self,value):
        self.value = value
        self.child = possible_states(value)
        self.worth = evaluate(value)
        self.o = list()
        for i in self.child:
            k=tree(self.child[i])
            self.o.append(k)
            s=evaluate(k.value)
            self.worth+=k.worth*0.1

def minmax(mou):
    if get_turn(mou)==1:
        if mou[1][1]==0:
            mou[1][1]-=1
        else:
            mou[0][2]-=1
        return mou
    test1=tree(mou)
    i=0
    k=0
    m=test1.o[0].worth
    while i<len(test1.o):
        if test1.o[i].worth<m:
            m=test1.o[i].worth
            k=i
        if evaluate(test1.o[i].value==-1):
            k = i
            break
        i += 1
    return test1.o[k].value