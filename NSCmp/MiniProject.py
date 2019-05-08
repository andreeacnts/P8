# -*- coding: utf-8 -*-
"""
MiniProject
"""

import numpy as np


n_vectors=20000
vector_dimension=2
data=np.random.uniform(-1, 1, size=(n_vectors, vector_dimension))
unif=np.random.uniform(size=n_vectors)
scale_f=np.expand_dims(np.linalg.norm(data, axis=1)/unif, axis=1)
data=data/scale_f

def gaussian(d, bw):
    return np.exp(-0.5*(d/bw)**2) / (bw*np.sqrt(2*np.pi))


#looped version
def _dist_poinc(a, b):
    num=np.dot(a-b, a-b)
    den1=1-np.dot(a,a)
    den2=1-np.dot(b,b)
    return np.arccosh(1+ 2* (num) / (den1*den2))
def dist_poinc(a, A):
    res=np.empty(A.shape[0])
    for i, el in enumerate(A):
        res[i]=_dist_poinc(a, el)
    return res

def meanshift(data, sigma, steps):
    d1 = np.copy(data)                        # Need to copy the data, don't want to modify the originals
    for it in range(steps):                   # at each step
        for i, p in enumerate(d1):            # for each point
            dists = dist_poinc( p, d1)        # we calculate the distance from that point to all the other ones
            weights = gaussian(dists, sigma)  # then we weight those distances by our gaussian kernel
            d1[i] = (np.expand_dims(weights,1)*d1).sum(0) / weights.sum()     # and substitute the point with the weighted sum
    return d1

#vectorized version
def num(points):
    expd=np.expand_dims(points,2) #need another dimension...
    tiled=np.tile(expd, points.shape[0]) #...to tile up the vectors
    trans=np.transpose(points) #Also need to transpose the points matrix to fit well with broadcasting
    diff=trans-tiled           #doing the difference, exploiting Numpy broadcasting capabilities
    num=np.sum(np.square(diff), axis=1) #an then obtain the squared norm of the difference
    return num

def den(points):
    sq_norm=1-np.sum(np.square(points),1) #subtracting from 1 the squared norm of the vectors
    expd=np.expand_dims(sq_norm,1)   #this operation is needed to obtain a correctly transposed version of the vector
    den_all=expd * expd.T #multiply the object by his transpose
    return den_all

def poinc_dist_vec(points):
    numa=num(points)
    dena=den(points)
    return np.arccosh(1+2*numa/ dena)

def meanshift_vec(points, sigma):
    dists=poinc_dist_vec(points) #the matrix of the distances
    weights = gaussian(dists, sigma) #the matrix of the weights
    expd_w=np.dot(weights, points) #the weighted vectors
    summed_weight=np.sum(weights,0) # the array of the summed weights, for normalize the weighted vectors
    shifted_pts=expd_w/np.expand_dims(summed_weight,1) #the normalized vectors
    return shifted_pts

#parallel version
import concurrent

def dist_batch(points,  n_begin, n_end):
    expd=np.expand_dims(points,2)
    tiled=np.tile(expd, n_end-n_begin)
    selected=points[n_begin:n_end]
    trans=np.transpose(selected)
    num=np.sum(np.square(trans-tiled), axis=1)

    den_sq_norm=1-np.sum(np.square(points),1)
    den_selected=den_sq_norm[n_begin:n_end]
    den_expd=np.expand_dims(den_sq_norm,1)
    den=den_expd * den_selected.T

    return np.arccosh(1+2*num/ den)

def __shift(data_all, sigma, beg, end):
    dists=dist_batch(data_all, beg, end)
    weights = gaussian(dists, sigma)
    expd_w=np.dot(weights.T, data_all)
    summed_weight=np.sum(weights,0)
    return expd_w/np.expand_dims(summed_weight,1), beg, end


def meanshift_parallel(data,sigma,  batches):
    pts = np.copy(data)
    n_samples=data.shape[0]
    processes_needed=int(np.ceil(n_samples/batches))
    maxworkers=min (6, processes_needed)

    with concurrent.futures.ThreadPoolExecutor(max_workers=maxworkers) as executor:
        future_shifted = {executor.submit(__shift, pts, sigma, d_beg, min(d_beg+batches, n_samples)):
                         d_beg for d_beg in range(0, n_samples, batches)}
        for future in concurrent.futures.as_completed(future_shifted):
            pts[future.result()[1]:future.result()[2]]=future.result()[0]
    return pts
         
            #For plotting the data
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,10))
ax = plt.gca()
ax.cla() # clear things for fresh plot

ax.set_xlim((-1.1, 1.1))
ax.set_ylim((-1.1, 1.1))
circle = plt.Circle((0,0), 1., color='black', fill=False)
ax.add_artist(circle)
plt.axis('off')
for point in data:
    ax.plot(point[0], point[1], 'o', color='b')
plt.show()

#to calculate the execution times
import timeit
times_looped=[]
times_parallel=[]


dim=[1000, 2000, 4000, 6000, 8000, 10000]
for i in dim:
    print (i)
    steps=2
    temp_times_looped=np.zeros(steps)
    temp_times_parallel=np.zeros(steps)
    for j in range(steps):
        print ("--", j)
        # looped
        start_time = timeit.default_timer()
        meanshift(data[:i], sigma=0.8, steps=1)
        temp_times_looped[j]=timeit.default_timer() - start_time
        
        # parallel, batch 100
        start_time = timeit.default_timer()
        meanshift_parallel(data[:i], sigma=0.8, batches=100)
        temp_times_parallel[j]=timeit.default_timer() - start_time
        
        
    temp_time_looped=np.sum(temp_times_looped)/temp_times_looped.shape[0]
    temp_time_parallel=np.sum(temp_times_parallel)/temp_times_parallel.shape[0]
    times_looped.append( temp_time_looped)
    times_parallel.append( temp_time_parallel)
    
    #Plot the execution times
from matplotlib import pyplot as plt
plt.plot(dim,times_parallel,label='batched & parallel, batch 100')

plt.plot(dim,times_looped,label='looped')


plt.legend()
plt.ylabel('Execution time')
plt.xlabel('number of vectors')
plt.yscale('log')
plt.show()

import matplotlib.ticker as mtick

percs=np.array(times_parallel)/np.array(times_looped)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(dim,percs*100,label='batched & parallel / looped')

ax.legend()
ax.set_ylabel('Execution time')
ax.set_xlabel('number of vectors')
fmt = '%.2f%%'
xticks = mtick.FormatStrFormatter(fmt)
ax.yaxis.set_major_formatter(xticks)
#plt.yscale('log')
#ax.set_ylim(0.20000, 0.630000)
plt.show()

