import numpy as np

#dataset
a = [12,13,14,15,10,16,10,109,13,12,16,101,25,19,20,16,12]

# quantile1 and quantile2
q1,q3 = np.percentile(a,[25,75])
print(q1,q3)

# inter-quantile range
iqr_value = q3-q1
print(iqr_value)
lower_bound_value = q1-(1.5*iqr_value)
upper_bound_value = q1+(1.5*iqr_value)
print(lower_bound_value,upper_bound_value)

print('original data set is ',a)

# removing outliers
for i in a:
    if i < lower_bound_value or i > upper_bound_value :
        a.remove(i)
print('Data set without outlier',a)

