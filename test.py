import numpy as np
import matplotlib.pyplot as plt
cityA=np.array([30, 32, 31, 29, 28, 27, 26])
cityB=np.array([35, 34, 36, 33, 32, 31, 30])
cityC=np.array([25, 26, 27, 28, 29, 30, 31])
cityD=np.array([22, 23, 24, 25, 26, 27, 28])
meanA=np.mean(cityA)
meanB=np.mean(cityB)
meanC=np.mean(cityC)
meanD=np.mean(cityD)
print(meanA)
print(meanB)
print(meanC)
print(meanD)
maxA=np.max(cityA)
maxB=np.max(cityB)
maxC=np.max(cityC)
maxD=np.max(cityD)
print("MAXIMUM TEMP")
print(maxA)
print(maxB)
print(maxC)
print(maxD)
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]  
def avg(a,b,c,d):
    m=(a+b+c+d)/4
    return m
for i in range(0,len(cityA)):
    ans=avg(cityA[i],cityB[i],cityC[i],cityD[i])
    print(days[i])
    print(ans)

  
plt.xlabel("DAYS")
plt.ylabel("Temp")

plt.plot(days,cityA);
plt.plot(days,cityB);
plt.plot(days,cityC);
plt.plot(days,cityD);
plt.legend("ABCD")
plt.show()

cityA=sorted(cityA)
lowA=cityA[0]
cityB=sorted(cityB)
lowB=cityB[0]
cityC=sorted(cityC)
lowC=cityC[0]
cityD=sorted(cityD)
lowD=cityD[0]
print("MiniMUM TEMP")
print(lowA)
print(lowB)
print(lowC)
print(lowD)

rangeA=maxA-lowA
rangeB=maxB-lowB
rangeC=maxC-lowC
rangeD=maxD-lowD
ranged=[rangeA,rangeB,rangeC,rangeD]
plt.bar(ranged,10)
plt.show()
