import math
import numpy as np
import matplotlib.pyplot as plt

e            = math.e
intens_coe   =   0.1
occur_thresh =   0.2
agent_num    =    11
iterations   =    40

# Definition function: agents interact with each other
def Agents_interaction(agents,agent_num,occur_thresh,intens_coe):
    agents_nextrow = list(agents[-1])
    agents_nextrow = [round(i,8) for i in agents_nextrow]
    random_coe = np.random.rand(agent_num,agent_num)
    list_interact = []
    for i in range(agent_num):
        t = i + 1
        while t < agent_num:
            if random_coe[i,t] >= occur_thresh:
               list_interact.append([i,t])
            t += 1
    np.random.shuffle(list_interact)
    for j in list_interact:
        agents_nextrow[j[0]],agents_nextrow[j[1]] \
        = agents_nextrow[j[0]] + intens_coe \
            * pow(10,(-1*abs(agents_nextrow[j[0]])))\
                    *pow(100,-1*(abs(agents_nextrow[j[0]]-agents_nextrow[j[1]]))) * agents_nextrow[j[1]],\
          agents_nextrow[j[1]] + intens_coe \
              * pow(10,(-1*abs(agents_nextrow[j[1]])))\
                      *pow(100,-1*(abs(agents_nextrow[j[0]]-agents_nextrow[j[1]]))) *  agents_nextrow[j[0]]
    agents = np.append(agents,[agents_nextrow],axis=0)
    return  agents
#Definition function:  Draw pictures to show agents' opinions
def Agents_mapping(agents):
    n,m = agents.shape
    for y in range(m):
        plt.plot(range(n),agents[:,y],'k-',linewidth=0.5)
    plt.xlabel('Number of iterations')
    plt.ylabel('Value of opinion')
    plt.ylim([-2,2])
    plt.show


#Initializes the agents opinion
agents = np.array([np.random.rand(agent_num)])
if agent_num % 2 == 0:
    for i in range(agent_num):
        if i < agent_num/2:
            agents[0,i]=i*(2/agent_num)-1
        else:
            agents[0,i]=(i+1)*2/agent_num-1
else:
    for i in range(agent_num):
        agents[0,i]=i*2/(agent_num-1)-1

#Play an iterative game
for x in range(iterations):
    
    agents = Agents_interaction(agents,agent_num,occur_thresh,intens_coe)


#Show the iterative game process in graph
Agents_mapping(agents)

