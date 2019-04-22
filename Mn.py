#!/usr/bin/env python
mode = 0
v1 = [[0,1,0,0,0,1]]
def computeMn(n):
	vList = { 1 : tuple(v1)}
	if n == 1: 
		return 1
	elif n < 1: 
		print("n should be a positiv integer != 0")
		return ""	
	for i in range(2,n+1):
		vTemp = []
		for j in range(1,i):
			vTemp = union(vTemp,composite(vList.get(j),vList.get(i-j)))
		vList.update({i : tuple(vTemp)})
		lastSet = vList.get(i)
		mn = maximum(lastSet)
		#print "n =:{} nth root of Mn:{} Mn:{} hull:{} Vn:{}".format(i,mn**(1/float(i)),maximum(lastSet),hull(lastSet),len(lastSet))
		print "{}&{}&{}&{}&{}".format(i,mn**(1/float(i)),maximum(lastSet),hull(lastSet),len(lastSet))
	#for k in range(1,n+1):
		#lastSet = vList.get(k)
		#print "n =:{} nth root of Mn:{} Mn:{} hull:{} Vn:{}".format(k,mn**(1/float(k)),maximum(lastSet),hull(lastSet),len(lastSet))
	lastSet = vList.get(n)
	
	return maximum(lastSet)
def maximum(lastSet):
	max = 0
	for k in range(len(lastSet)):
		sum = mAddition(lastSet[k])
		if max < sum:
			max = sum
	return max	
def hull(lastSet):
	nonSkip = range(len(lastSet))	
	for i in range(len(lastSet)):
		if i not in nonSkip:
			continue	
		for k in range(i+1,len(lastSet)):
			comparison = hullSumCompare(lastSet[i],lastSet[k])
			if comparison == 0:
				if k in nonSkip:
					nonSkip.remove(k)
			elif comparison == 1:
				if i in nonSkip:
					nonSkip.remove(i)					
	return len(nonSkip)		
				
def hullSumCompare(vSet1,vSet2):
	vSetSum1 = hullSum(vSet1)
	vSetSum2 = hullSum(vSet2)
	oneIsGreater = 0
	for i in range(len(vSet1)):
		if(vSetSum1[i]>vSetSum2[i]):
			oneIsGreater += 1
	if oneIsGreater == 0:
		return 0
	elif oneIsGreater == len(vSet1):
		return 1
	else:
		return 2
def hullSum(vSet):
	return [vSet[0],vSet[0]+vSet[1],vSet[0]+vSet[1]+vSet[2],vSet[3],vSet[3]+vSet[4],vSet[5]]		
def composite(list1,list2):
	composition = []
	for i in range(len(list1)):
		for j in range(len(list2)):			
			composition.append(product(list1[i],list2[j]))
	return composition		
def product(v1,v2):
	if mode == 1:
		return [v1[0]*v2[5]+v1[1]*v2[5]+v1[2]*v2[5]+v1[0]+v2[3],
		v1[1]*v2[3],
		v1[2]*v2[3],
		v1[3]*v2[0]+v1[3]*v2[1]+v1[3]*v2[3]+v1[3]*v2[4]+v1[5]*v2[0]+v1[5]*v2[1],
		v1[4]*v2[3]+v1[4]*v2[4]+v1[5]*v2[2],
		v1[5]*v2[3]+v1[5]*v2[4]]

	elif mode == 2:
		return [v1[1]*v2[5]+v1[0]*v2[5],
		0,
		0,
		v1[3]*v2[3]+v1[3]*v2[4]+v1[5]*v2[0]+v1[5]*v2[1],
		v1[4]*v2[3]+v1[4]*v2[4]+v1[5]*v2[2],
		v1[5]*v2[3]+v1[5]*v2[4]]

	else:
		return [v1[0]*v2[0]+v1[0]*v2[3]+v1[0]*v2[5]+v1[1]*v2[5]+v1[2]*v2[5],
		v1[1]*v2[3],
		v1[1]*v2[0]+v1[2]*v2[0]+v1[2]*v2[3],
		v1[3]*v2[0]+v1[3]*v2[1]+v1[3]*v2[3]+v1[3]*v2[4]+v1[5]*v2[0]+v1[5]*v2[1],
		v1[4]*v2[3]+v1[4]*v2[4]+v1[5]*v2[2],
		v1[5]*v2[3]+v1[5]*v2[4]]	
def mAddition(a):
	return a[0]+a[1]+a[3]+a[4]
def union(list1, list2):
    u = []
    for x in list1 :
        u.append(x)  
    for x in list2:
        if (x not in u) :  u.append(x)
    return u
n = 0
print("exit criteria: type a neg. number as input")
print("modes: 1 for Def 1, 2 for Def.2, else for normal mode ")
while n >= 0:	#exit criteria: n<0		
	n = int(input("positiv integer for n: "))
	if(n < 0):break
	mode = int(input("positiv integer for mode: "))
	if(mode < 1):break
	output = computeMn(n)
	print "The maximum number of dominated sets for the given n and mode is: {}".format(output)


