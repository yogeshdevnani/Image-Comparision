from PIL import Image
import numpy as np

img =  Image.open('Data/img_blue.PNG')
matrix = np.array(img)


print ("\t\t\tShape = {}\t".format(matrix.shape))
print ("\n"*2)

x_i = len(matrix)
x_j = len(matrix[0])
x_k = len(matrix[0][0])
ctr=0
for i in range(x_i):
    for j in range(x_j):
        print ("[",end="")
        for k in range(x_k):
            print (matrix[i][j][k],end=" ")
            ctr+=1
        print ("]",end="")
        if j%6==0:
            print ("\n")
    print ("\n")
    print ("-j-"*15)


print ("\n"*2)
print ("Ctr = {}".format(ctr))
print ("\t\t\tShape = {}\t".format(matrix.shape))
