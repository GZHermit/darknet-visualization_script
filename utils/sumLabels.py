import os
path ='./labels/'
names = os.listdir(path)
nums = [0 for i in range(5)]
for name in names:
    with open(path+name,'r') as f:
        lines = f.readlines()
	for line in lines:
            classes = int(line.split()[0])
            nums[classes] += 1
sums = 0
for i in range(5):
    sums += nums[i]
print("sums:{}".format(sums))
for i in range(5):
    print("class:{},rate:{}".format(i,float(float(nums[i])/sums)))


