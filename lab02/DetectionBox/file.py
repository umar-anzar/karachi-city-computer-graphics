from PIL import Image
import numpy as np





with Image.open("2a.png") as im:
    im = im.convert('1')
    arr = np.array(im)





black_arr_x = []
black_arr_y = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]==False:
            black_arr_y.append(i)
            black_arr_x.append(j)

max_x, max_y = max(black_arr_x), max(black_arr_y)
min_x, min_y = min(black_arr_x), min(black_arr_y)


class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y



'''
D-------------C
|             |
|             |
|             |
|             |
A-------------B
'''

A = Coordinate(min_x, max_y)#left bottom
B = Coordinate(max_x, max_y)#right bottom
C = Coordinate(max_x, min_y)#right top
D = Coordinate(min_x, min_y)#left top


for i in range(A.x,B.x):
    arr[A.y][i] = False
    arr[D.y][i] = False

for i in range(D.y,A.y):
    arr[i][A.x] = False
    arr[i][C.x] = False





image = Image.fromarray(arr)
image.save('detect2a.png')

