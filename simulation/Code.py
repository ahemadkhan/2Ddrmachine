#import imutils
import numpy as np
import matplotlib.pyplot as plt 
import cv2
import serial
import pandas as pd
import math
import numpy
image = cv2.imread("lt.jpg")
#cv2.imshow("orifginal",image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(thresh, BWImage) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Black white image', BWImage)
#cv2.imshow("Image", image)
#cv2.imshow("Grayscale",gray)
scale_percent = 80
width = int(image.shape[1] * scale_percent / 200)
height = int(image.shape[0] * scale_percent / 200)
dim = (width, height)
# resize image
resized = cv2.resize(BWImage, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("150",resized)
m=0
for i in range(0,resized.shape[0]):
    for j in range(0,resized.shape[1]):
        if resized[i][j]==0:
            m+=1
print(m)
arr = [[0 for i in range(2)] for j in range(m)]
l=0
for i in range(0,resized.shape[0]):
    for j in range(0,resized.shape[1]):
        if resized[i][j]==0:
            arr[l][0]=i
            arr[l][1]=j
            l+=1
#print(arr)
a = [[0 for i in range(l)] for j in range(l)]
k = [0 for i in range(l)]
mn=0
visited_m = [0 for i in range(l)]

for t in range(0,l):
    for h in range(0,l):
        a[t][h] = (arr[t][0]-arr[h][0])*(arr[t][0]-arr[h][0]) + (arr[t][1]-arr[h][1])*(arr[t][1]-arr[h][1])


order_final=[]
#plt.plot(arr)
w = 0
jk=0
#pure pe sath me dfs
while(1):
	curr_min=1000000
	for i in range(0,l):
		if visited_m[i]==0:
			if curr_min>a[i][w]:
				curr_min=a[i][w]
				r = i		
	w=r
	order_final.append(w)
	visited_m[w]=1
	jk+=1
	if jk==l:
		break
#x = np.array(order_final) 
#order_finall = np.array(order_final)
#order_final.flatten()
#print(ini_array)
#np.reshape(x, (1536, 1))
#print (x) 
print("saare loop khatam ho gaye check")
print(order_final)
k=order_final
print(l)
#print(k)
#plt.plot(arr[k][0],arr[k][1])
#plt.show()

#copiedcodefrom here
x_array = [0 for i in range(l)]
y_array = [0 for i in range(l)]
for j in range(0,l):
    x_array[j] = arr[k[j]][0]
    y_array[j] = arr[k[j]][1]
plt.scatter(x_array,y_array,color="green")

p=[]
#p.append(0)
for j in range(0,l-1):
    if a[k[j]][k[j+1]]<2:
        p.append(1)
    else:
        p.append(0)
print(len(p))
p.append(0)

l1 = 353.624
l2 = 353.624
  
#l1 = 800
#l2 = 800
for i in range (0,l):
    x_array[i]=x_array[i]+1
    y_array[i]=y_array[i]+1
alpha = [0 for i in range(0,l)]
beta = [0 for i in range(0,l)]
for i in range(0,l):
    alpha[i]  = (math.pi/2) + math.atan(y_array[i]/x_array[i]) -(1/2)*math.acos(1-(x_array[i]*x_array[i] + y_array[i]*y_array[i])/(2*l1*l2))
    beta[i] = math.acos(1-(x_array[i]*x_array[i] + y_array[i]*y_array[i])/(2*l1*l2)) - math.pi

print(alpha,beta)

print(len(p),p)

alpha = numpy.asarray(alpha)
beta = numpy.asarray(beta)
p = numpy.asarray(p)
a = numpy.asarray([(alpha),(beta),(p)])
numpy.savetxt("Image1.csv",a,delimiter=";",fmt='%f')

#a1 = numpy.concatenate((alpha,beta,p))
#df = pd.DataFrame(a1,columns = ['alpha','beta','p'])
#df.to_csv(r'./CSV_col1.csv')
  
plt.xlabel('x - axis') 
# frequency label 
plt.ylabel('y - axis') 
# plot title 
plt.title('My scatter plot!') 
# showing legend
# function to show the plot 
plt.show()
#print(BWImage.shape[1])
#model = Sequential([MaxPooling2D(pool_size = 2, strides = 2)]) 
#output1 = model.predict(BWImage)
#cv2.imshow('Black white image', output1)
#print(BWImage)
cv2.waitKey(0)