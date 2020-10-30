
'''
p=[0.2, 0.2, 0.2, 0.2,0.2]
world=['green', 'red', 'red', 'red', 'green', 'green']
Z = 'green'
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
'''

#what would this look like if I had two measurements? Let's find out
'''
p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q
#
#ADD YOUR CODE HERE

for k in range(len(measurements)):
    p = sense(p, measurements[k])
#

print(p)

#This solution will work for measurements of any lenght! How cool is that?
'''
#Program a function that returns a new distribution 
#q, shifted to the right by U units. If U=0, q should 
#be the same as p.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    #
    #ADD CODE HERE
    q=[]
    for i in range(len(p)):
        q.append(p[(i-U) % len(p)])
    #
    return q

print(move(p, 4))

