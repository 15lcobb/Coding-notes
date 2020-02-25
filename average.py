gg = [1,2,3,4,5,6]

#range
print(len(gg)-gg[0])

#mean
print(sum(gg)/len(gg))

#median
n = len(gg) 
gg.sort() 
  
if n % 2 == 0: 
    median1 = gg[n//2] 
    median2 = gg[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = gg[n//2] 
print("Median is: " + str(median)) 

#mode
y = max(set(gg),key = gg.count)
print(y)
