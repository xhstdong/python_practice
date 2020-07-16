# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:32:53 2020

@author: stdon
"""

import timeit
import random
import time
#import matplotlib.pyplot as plt

#result=[]
#size=[]
for size in range(100000, 1000001,100000):
#     t = timeit.Timer('x[random.randrange(%d)]'%size, 'from __main__ import random, x')
#     x=list(range(size))

#     result_time = t.timeit(number=1000) 
#     print('list: run time for {} elements is {:.8}'.format(size, result_time))
#     x = {j:None for j in range(size)}
#     #t = timeit.Timer('x.get(random.randrange(%d))'%size, 'from __main__ import random, x')
#     result_time=t.timeit(number=1000)
#     print('dictionary: run time for {} elements is {:.8}'.format(size, result_time))
# #    size.append(size)
# #    result.append(index_time)
    x=list(range(size))
    start=time.time()
    del x
    elapsed = time.time()-start
    print('list: run time for {} elements is {:.8}'.format(size, elapsed))
    
    x = {j:None for j in range(size)}
    start=time.time()
    del x
    elapsed = time.time()-start
    print('dict: run time for {} elements is {:.8}'.format(size, elapsed))