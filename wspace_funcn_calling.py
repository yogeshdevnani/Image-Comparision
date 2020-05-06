from PIL import Image
import numpy as np

#Similarity Calculator
def recognize(image_a,image_b):
    height = min(len(image_a),len(image_b))
    width = min(len(image_a[0]),len(image_b))
    similarity = 0
    for i in range(height):
        for j in range(width):
            if image_a[i][j] == image_b[i][j]:
                similarity+=1
    similarity = (similarity/(height*width))*100
    return similarity



#Display Area
def display(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print (matrix[i][j],end=" ")
        print ("\n")



# Specification Printing Area
def specs():
    print ("Shape = {}".format(np_matrix.shape))

def max_pixel(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = max(matrix[i][j][:3])

    return matrix

def comp_reduce(matrix):    #Compare and Reduce
    #Assuming we get 2d array
    if len(matrix) < 100 and len(matrix[0]) < 100:        #what if the ratio is f*cked up? like in place of or?
        return matrix
    ans = []
    for i in range(0, len(matrix)-3,3):
        line = []
        for j in range(0,len(matrix[0])-3,3): #What if i or j=13 when len = 14
            t = max(max(matrix[i][j:j+3]),max(matrix[i+1][j:j+3]),max(matrix[i+2][j:j+3]))
            line.append(t)
        ans.append(line)

    return comp_reduce(ans)

#Main Area
def main():
    #Image 1
    img_1_loc = input("Image 1 : ")
    img_1_loc = "Data" + chr(47) + img_1_loc + ".png"
    img_1 = Image.open(img_1_loc)
    np_matrix_1 = np.array(img_1)
    matrix_1= np_matrix_1.tolist() #Converting to normal Python List
    matrix_1 = max_pixel(matrix_1)
    matrix_1 = comp_reduce(matrix_1)
    #display(matrix_1)

    print ("\n","-"*40,"\n")

    #Image 2
    img_2_loc = input("Image 2 : ")
    img_2_loc = "Data" + chr(47) + img_2_loc + ".png"
    img_2 = Image.open(img_2_loc)
    np_matrix_2 = np.array(img_2)
    matrix_2 = np_matrix_2.tolist()
    matrix_2 = max_pixel(matrix_2)
    matrix_2 = comp_reduce(matrix_2)
    #display(matrix_2)

    print ("\n\n\n\n\n\n\n\n")
    print ("\t\t\t",recognize(matrix_1,matrix_2),"%")

main()


