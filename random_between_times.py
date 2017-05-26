from random import *
from time import *


date1 = (2009,2,2,0,0,0,-1,-1,-1)
date2 = (2017,1,17,0,0,0,-1,-1,-1)

time1 = mktime(date1)
time2 = mktime(date2)

random_time = uniform(time1,time2)

print asctime(localtime(random_time))