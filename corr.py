from scipy.stats.stats import pearsonr
import numpy
import json
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

def remove_mean(x):
    mean =  numpy.mean(x)
    x_m = x[:] - mean
    return x_m

def normalize(x):
    minv = min(x)
    maxv = max(x)
    di = (maxv - minv)
    x_n = (x[:] - minv) / di
    return x_n 

f = open('adsquare_teaser_dataMay2014.json')
data = json.load(f)
f.close()
indx = data['Index']
indexkeys = indx.values()

len = max(indexkeys) + 1
len = int(len)
x1 = [0]*len
x2 = [0]*len
x3 = [0]*len
x4 = [0]*len 
x5 = [0]*len
ear = [0]*len

for key in data['X1']:
    x1[int(key)] = data['X1'][key]

for key in data['X2']:
    x2[int(key)] = data['X2'][key]

for key in data['X3']:
    x3[int(key)] = data['X3'][key]

for key in data['X4']:
    x4[int(key)] = data['X4'][key]

for key in data['X5']:
    x5[int(key)] = data['X5'][key]

for key in data['Earning']:
    ear[int(key)] = data['Earning'][key]    


xrange = range(0, len)

x2_m = remove_mean(x2)
x2_n = normalize(x2_m)

x1_m = remove_mean(x1)
x1_n = normalize(x1_m)

x3_m = remove_mean(x3)
x3_n = normalize(x3_m)

x4_m = remove_mean(x4)
x4_n = normalize(x4_m)

x5_m = remove_mean(x5)
x5_n = normalize(x5_m)

ax.plot(xrange, x2_n)

ear_m = remove_mean(ear)
ear_n = normalize(ear_m)




#ax.plot(xrange, ear_n)

#print pearsonr(x2_n,ear_n)
#print pearsonr(x2_m,ear_m)
#print pearsonr(x2,ear)

z = numpy.vstack((x2_n, ear_n))
c = numpy.cov(z.T)
print c

'''
for i in range(0,len):
    print x1_n[i], x2_n[i], x3_n[i], x4_n[i], x5_n[i], ear_n[i]
'''


#plt.show()
'''
print pearsonr(x1,ear)
print pearsonr(x2,ear)
print pearsonr(x3,ear)
print pearsonr(x4,ear)
print pearsonr(x5,ear)
'''





'''
f = open('corr.data')
a = f.read()
lines = a.split("\n")
x1 = []
x2 = []
for l in lines:
    x1.append(int(l.split("\t")[0]))
    x2.append(int(l.split("\t")[1]))
    
print pearsonr(x1,x2)
'''