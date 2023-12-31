import numpy as np

a = [12,13,14,15,10,16,10,109,13,12,16,101,25,19,20,16,12]
print("dataset with outliers",a)

mean = int(np.mean(a))             # mean value
print("mean is = ",mean)

deviation = int(np.std(a))         # standard deviation
print("standard deviation = ",deviation)

threshold_value = 2

for i in a:
    z_score = int((i-mean)/deviation)
    if np.abs(z_score) >= threshold_value   :
        a.remove(i)
        
print("dataset without outliers",a)
