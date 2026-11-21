import numpy as np
arr = np.array([10,20,30,40,50])
print(arr)

print ("maximum value:",np.max(arr))


print ("minimum value:",np.min(arr))
print ("sum of values:",np.sum(arr))
print("average:",np.average(arr))

arr =np.array([[1,2,3,4],[5,6,7,8]])
print("shape:",arr.shape)
print("size:",arr.size)
print("dimensions:",arr.ndim)
arr =np.array([50,40,60,20,10])
print(np.sort(arr))

arr =np.array([1,2,3,4,5,6,7,8])
result = arr.reshape(2,3)
print(result)