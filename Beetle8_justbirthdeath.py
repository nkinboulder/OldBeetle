import numpy as np
import matplotlib.pyplot as plt


class Beetle(object):
    def __init__(self, beetlename, betak=3.0, betatheta=1, alphak=0.0001, alphatheta=1, container=0):
        self.beetlename = beetlename
        self.sex = np.random.binomial(1,femalefreq) #0=male, 1=female
        self.container = container
        #self.D = 0 #dispersal tendency
        self.beta = np.random.gamma(betak,betatheta) #egg laying tendency; first value k (shape), second value theta (scale)
        #these are floats -- if I get exponential pop growth, this can crash the program.
        self.alpha = np.random.gamma(alphak,alphatheta) #egg eating rate;
        #self.stage = 0 #0 is egg, 1 is adult
        self.trait = np.random.binomial(1,0.5)
    def disperse(self, NewContainer):
        self.container = NewContainer

def dispersal(beetle, outputarray):
    NewContainer=-1
    while NewContainer<0:
        L=np.random.normal() #how much beetle will disperse; positive = increase in container; neg = decrease
        NewContainer = int(L) + beetle.container #add dispersal distance to current container location value
    if abs(L)>=1: #only update container if beetle moves by at least 1 (one container)
        if NewContainer >= numContainers: #if NewContainer is too high, upper bound acts as reflecting boundary
            NewContainer=(numContainers-1) - (NewContainer-numContainers)
        beetle.disperse(NewContainer) #update beetle's self.container
    outputarray.append(beetle) #put beetle into outputarray (afterdispersal)
    return

def nextgen(CurrentGen):
    numEggsbyContainer=np.zeros(numContainers, dtype=int) #initialize new numEggs to all be 0 by default
    for beetle in afterdispersal: #after beetles have dispersed:
        if beetle.sex ==1: #if they are female
            numEggsbyContainer[beetle.container]+=(np.random.poisson(beetle.beta)) #update numEggs[container beetle is in after dispersal]
        numEggsbyContainer[beetle.container]-=(np.random.poisson(beetle.alpha))#all adults go around eating eggs in their own container
    for x in range(len(numEggs)): #for each index of numEggs
        if numEggsbyContainer[x]<0: #if, after birth/death, numEggs[x]<0
            numEggsbyContainer[x]=0 #make numEggs[x]=0
    #print numEggs
    return numEggsbyContainer

N=10
femalefreq=0.5
numContainers=10
generations=20
beforedispersal=[]
afterdispersal=[]
output=[]
i=0 #index for unique beetle naming

#initialize my output array with lots of zeros.
output.append([])
output[0].append(N)
for i in range(numContainers -1): ##Should this be number of containers? or num generations?
	output[0].append(0)

print output

#set up beforedispersal for generation 0 to get things rolling:
def initialize_before_dispersal(N):
    i=0
    for n in range(N):
        beforedispersal.append(Beetle(i, container=0))
        i+=1
    print beforedispersal
    return i

def dispersal_only_function(inputlist):
    num_beetles_per_container=[]
    for i in range(numContainers):
        num_beetles_per_container.append(0)
    for beetleobject in inputlist:
        num_beetles_per_container[beetleobject.container]+=1
    return num_beetles_per_container

def no_dispersal_just_growth(inputlist):
    for beetle in inputlist:
        afterdispersal.append(beetle)
    return afterdispersal
        

initialize_before_dispersal(N)



for g in range(generations):
    #afterdispersal=[]
    #no_dispersal_just_growth(beforedispersal)
    for beetle in beforedispersal:
        dispersal(beetle, afterdispersal) #disperse each beetle
    print 
    
    N=0
    for beetle in afterdispersal:
        N+=1
    if N < 0:
        print "Houston, we have a problem."
    #print 'N is ', N
    newbeetles=nextgen(afterdispersal) #newbeetles = output of nextgen, NumEggs, type = numpy array
    #newbeetles=dispersal_only_function(afterdispersal)
    beforedispersal=[] #reset beforedispersal to empty list
    output.append(newbeetles)  #now we're going to output important data to output
    for j in range(len(newbeetles)):
        for k in range(newbeetles[j]): #newbeetles[j] type = int
            beforedispersal.append(Beetle(i, container=j)) #now put the next gen of beetles into beforedispersal
            i+=1 #change i index for beetle naming

P=[] #P is just a list to use for plotting
for c in range(numContainers):
    P.append([])
    for g in range(generations+1):
        P[c].append(output[g][c])
for i in range(len(P)):
    plt.plot(P[i], color='gray')
#plt.plot(P[i], label='$C = %i$' %(i+1), color='gray')
#plt.legend() #adds legend with labels
#plt.xlabel('generations')
#plt.ylabel('Population size')
#plt.title('Population size over time')
#plt.show()

       

    '''




        






