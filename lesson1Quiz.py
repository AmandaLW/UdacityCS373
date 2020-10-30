p=[0.2, 0.2, 0.2, 0.2,0.2]
world=['green', 'red', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

#The sense function is the heart of localization! 
def sense(p,Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i]*(hit * pHit + (1-hit) *pMiss))
    s=sum(q)
    for i in range(len(q)):
        q[i] = q[i] /s
    return q

print(sense(p, Z))