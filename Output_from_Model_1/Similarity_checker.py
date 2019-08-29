import numpy as np

imp_arr = np.load("Imputed_All_GT.npy")
total_arr = np.load("Test_array_ALL_GT.npy")
print(imp_arr.shape)
print(total_arr.shape)
mismatch_cnt = 0

for i in range(imp_arr.shape[0]):
	print("Checking tree -> " + str(i))
	mismatch_cnt = 0
	for j in range(len(imp_arr[i])):
		x = np.argmax(imp_arr[i][j])
		y = np.argmax(total_arr[i][j])
		if(x != y):
			mismatch_cnt += 1
			print("Mismatch at j " + str(j) + " " + str(imp_arr[i][j]) + " " + str(total_arr[i][j]))
	print("Mismatch count = " + str(mismatch_cnt))
#print(arr[0])